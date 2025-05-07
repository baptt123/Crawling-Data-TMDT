from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import mysql.connector
import time
import re

# Cấu hình Chrome
chrome_options = Options()
chrome_options.add_argument("--headless")  # chạy nền
driver = webdriver.Chrome(service=Service(), options=chrome_options)

# Mở trang web
driver.get("https://nguyenson.vn/collections/banh-sinh-nhat")  # Thay bằng URL thật
time.sleep(3)  # Đợi trang tải (nên dùng WebDriverWait nếu cần ổn định hơn)

# Kết nối CSDL
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="tmdt"
)
cursor = db.cursor()

# Tìm tất cả sản phẩm
product_blocks = driver.find_elements(By.CLASS_NAME, "product-block")

for block in product_blocks:
    try:
        # Tên sản phẩm
        name = block.find_element(By.CSS_SELECTOR, ".pro-name a").text.strip()

        # Mô tả (không có -> gán mặc định)
        description = "Sản phẩm ngon tuyệt!"  # hoặc có thể lấy từ trang chi tiết nếu cần

        # Giá sản phẩm
        price_text = block.find_element(By.CSS_SELECTOR, ".pro-price span").text.strip()
        price = float(re.sub(r"[^\d]", "", price_text))  # loại ₫ và dấu phẩy

        # Ảnh sản phẩm
        image_tag = block.find_element(By.CSS_SELECTOR, "img.img-loop")
        image_url = image_tag.get_attribute("data-src")
        if image_url.startswith("//"):
            image_url = "https:" + image_url

        # Các trường khác
        stock = 10
        category_id = 4

        # Câu SQL
        sql = """
            INSERT INTO products (name, description, price, stock, image_url, category_id)
            VALUES (%s, %s, %s, %s, %s, %s)
        """
        cursor.execute(sql, (name, description, price, stock, image_url, category_id))
        db.commit()
        print(f"Đã lưu: {name}")
    except Exception as e:
        print("Lỗi khi xử lý sản phẩm:", e)

# Đóng
cursor.close()
db.close()
driver.quit()
