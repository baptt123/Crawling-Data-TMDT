from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager  # Tự động tải chromedriver

# Cấu hình Service cho chromedriver
service = Service(ChromeDriverManager().install())

# Khởi tạo trình duyệt Chrome
driver = webdriver.Chrome(service=service)

# Mở trang web
url = 'https://anhhoabakery.vn/'  # URL của trang bạn muốn crawl
driver.get(url)

# Lấy tất cả các thẻ div có class 'grid__item'
products = driver.find_elements(By.CLASS_NAME, 'grid__item')

# Lặp qua từng sản phẩm và lấy thông tin
for product in products:
    try:
        # Lấy tên sản phẩm
        title = product.find_element(By.CSS_SELECTOR, 'div.product-title a').text

        # Lấy giá sản phẩm
        price = product.find_element(By.CSS_SELECTOR, 'div.product-price').text

        # Lấy liên kết sản phẩm
        link = product.find_element(By.CSS_SELECTOR, 'div.product-img a').get_attribute('href')

        # Lấy link ảnh sản phẩm
        img_url = product.find_element(By.CSS_SELECTOR, 'div.product-img img').get_attribute('src')

        # In kết quả
        print(f'Tên sản phẩm: {title}')
        print(f'Giá: {price}')
        print(f'Link sản phẩm: {link}')
        print(f'Link ảnh sản phẩm: {img_url}')
        print('-' * 40)
    except Exception as e:
        print(f'Lỗi khi lấy dữ liệu sản phẩm: {e}')

# Đóng trình duyệt
driver.quit()
