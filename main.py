import traceback

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

from utils.output_utils import print_inf

# 启动chrome selenium
opt = Options()
# opt.add_argument('--headless')
cdriver = webdriver.Chrome('chromedriver/chromedriver.exe', options=opt)  # win c driver
cdriver.implicitly_wait(0.0001)  # wait
print_inf('selenium启动成功')
if __name__ == '__main__':

    cdriver.get('http://jlh.125ks.cn/cxk/bccxk/')
    cdriver.find_element(By.XPATH, '//*[@id="btn_group"]/a[1]').click()  # 开始
    c = 0
    while True:
        c += 1
        if c >= 3:
            c = 1
        for i in range(0, 37):
            try:
                # print('%s-%s'%(c,i))
                f1 = '//*[@id="GameLayer%s-%s"]' % (c, i + 0)
                f2 = '//*[@id="GameLayer%s-%s"]' % (c, i + 1)
                f3 = '//*[@id="GameLayer%s-%s"]' % (c, i + 2)
                f4 = '//*[@id="GameLayer%s-%s"]' % (c, i + 3)
                l1 = cdriver.find_element(By.XPATH, f1)
                l2 = cdriver.find_element(By.XPATH, f2)
                l3 = cdriver.find_element(By.XPATH, f3)
                l4 = cdriver.find_element(By.XPATH, f4)
                x1 = l1.value_of_css_property('background-image')
                x2 = l2.value_of_css_property('background-image')
                x3 = l3.value_of_css_property('background-image')
                x4 = l4.value_of_css_property('background-image')
                if 'png' in x1:
                    l1.click()
                elif 'png' in x2:
                    l2.click()
                elif 'png' in x3:
                    l3.click()
                elif 'png' in x4:
                    l4.click()
            except Exception:
                # traceback.print_exc()
                pass

