from selenium import webdriver
import time
import read
from selenium.webdriver.support.select import Select
import selenium.webdriver.support.ui as ui

result=[] #全局变量
dic = {'108':('_p90311370','_p90311370k51984422','showcolor90311370','_p90311370k51964227e5952770TD'),
       '138':('_p90343399','_p90343399k51984422','showcolor90343399','_p90343399k51976539e5952830TD'),
       '218':('_p90343406','_p90343406k51984422','showcolor90343406','_p90343406k51976546e5952970TD'),
       '238':('_p90343407','_p90343407k51984422','showcolor90343407','_p90343407k51976547e5952990TD'),
       '258':('_p90343408','_p90343408k51984422','showcolor90343408','_p90343408k51976548e5953010TD'),
       '98':('_p90311373','_p90311373k51984422','showcolor90311373','_p90311373k51964232e5952750TD'),
       '118':('_p90343397','_p90343397k51984422','showcolor90343397','_p90343397k51976537e5952790TD'),
       '128':('_p90343398','_p90343398k51984422','showcolor90343398','_p90343398k51976538e5952810TD'),
       '138':('_p90343399','_p90343399k51984422','showcolor90343399','_p90343399k51976539e5952830TD'),
       '148':('_p90343400','_p90343400k51984422','showcolor90343400','_p90343400k51976540e5952850TD'),
       '158':('_p90343401','_p90343401k51984422','showcolor90343401','_p90343401k51976541e5952870TD'),
       '168':('_p90343402','_p90343402k51984422','showcolor90343402','_p90343402k51976542e5952890TD'),
       '178':('_p90343403','_p90343403k51984422','showcolor90343403','_p90343403k51976543e5952910TD'),
       '188':('_p90343404','_p90343404k51984422','showcolor90343404','_p90343404k51976544e5952930TD'),
       '198':('_p90343405','_p90343405k51984422','showcolor90343405','_p90343405k51976545e5952950TD'),
       '278':('_p90343409','_p90343409k51984422','showcolor90343409','_p90343409k51976549e5953030TD'),
       '298':('_p90343410','_p90343410k51984422','showcolor90343410','_p90343410k51976550e5953050TD'),
       '318':('_p90343411','_p90343411k51984422','showcolor90343411','_p90343411k51976551e5953070TD'),
       '358':('_p90343412','_p90343412k51984422','showcolor90343412','_p90343412k51976552e5953090TD'),
       '398':('_p90343420','_p90343420k51984422','showcolor90343420','_p90343420k51976561e5953110TD'),
       '48':('_p90363849','','showcolor90363849','_p90363849k51999456e8351474TD'),
       '58':('_p90363850','','showcolor90363850','_p90363850k51999457e8351529TD'),
       '68':('_p90363851','','showcolor90363851','_p90363851k51999458e8351573TD'),
       '78':('_p90363852','','showcolor90363852','_p90363852k51999459e8351551TD'),
       '88':('_p90363853','','showcolor90363853','_p90363853k51999460e8351595TD'),
       }

def login(driver):
    driver.find_element_by_id('STAFF_ID').send_keys('')
    driver.find_element_by_id('LOGIN_PASSWORD').send_keys('')
    province=driver.find_element_by_id('LOGIN_PROVINCE_CODE')
    Select(province).select_by_value('51')
    vcode = input("verifyCode:")
    driver.find_element_by_id('VERIFY_CODE').send_keys(vcode)
    driver.find_element_by_xpath('//*[@class="submit clear"]/input[1]').click()

    SMS = input("SMS:")
    driver.find_element_by_css_selector("input[name='SMS_VERIFY_CODE']").send_keys(SMS)
    driver.find_element_by_id('bsubmit').click()

    return driver

def nav0(driver):
    input('change to 服务号码')
    driver.switch_to_frame('contentframe')
    driver.switch_to_frame('navframe_0')
    driver.switch_to_frame('chkcustframe')
    driver.find_element_by_id('SERIAL_NUMBER').send_keys('18565099490')
    driver.find_element_by_id('bssbutton').click()
    time.sleep(1)
    driver.switch_to.default_content()
    driver.switch_to_frame('sidebarframe')
    driver.find_element_by_css_selector("a[value='移网产品/服务变更']").click()
    return driver

def nav1(driver,tc,phone,people):
    driver.switch_to.default_content()
    driver.switch_to_frame('contentframe')
    driver.switch_to_frame('navframe_1')
    driver.find_element_by_id('SERIAL_NUMBER').clear()
    driver.find_element_by_id('SERIAL_NUMBER').send_keys(phone)
    #查询
    driver.find_element_by_id('queryTrade').click()
    #解决弹窗
    try:
        driver.find_element_by_css_selector("input[value=' 确定 ']").click()
    except Exception as e:
        pass
    time.sleep(2)

    #搜索套餐
    try:
        driver.find_element_by_id('queryProductName').send_keys(tc)
    except Exception:
        result.append(["失败","用户不存在或已停机或有未完成订单",phone])
        return driver
    driver.find_element_by_id('productNameQuery').click()
    time.sleep(0.5)
    #判断是否做过
    bql=driver.find_element_by_id(dic[tc][2])
    if bql.get_attribute("style")=="COLOR: #f75000":
        result.append(["成功","",phone])
        return driver
    #逐个点击直到找到原有基本套餐
    pros=driver.find_elements_by_name('_productinfos')
    for pro in pros:
        pro.click()
        try:
            driver.find_element_by_css_selector("input[value=' 确定 ']").click()
            break
        except Exception as e:
            pass
        pro.click()
    #选套餐
    driver.find_element_by_id(dic[tc][0]).click()
    time.sleep(2)
    #对所有弹出选框选择确定
    while(1):
        try:
            target=driver.find_element_by_css_selector("input[value=' 确定 ']")
            driver.execute_script("arguments[0].scrollIntoView();", target)
            target.click()
        except Exception as e:
            break
    #如果已有冰淇淋套餐，这里会报错
    try:
        driver.find_element_by_id(dic[tc][3]).click()
    except Exception:
        result.append(["失败","已存在其他冰淇淋套餐",phone])
        return driver

    driver.find_element_by_id('REMARK').send_keys(people)
    driver.find_element_by_id('submitTrade').click()
    driver.find_element_by_css_selector("input[value=' 确定 ']").click()
    # wait1 = ui.WebDriverWait(driver,3)
    # #判断有无出错
    # try:
    #     wait1.until(lambda driver:driver.find_element_by_link_text("系统错误"))
    #     result.append(["失败","系统错误",phone])
    #     input("记录错误")
    #     driver.find_element_by_css_selector("input[value=' 确定 ']").click()
    #     return driver
    # except Exception as e:
    #     pass
    while(1):
        try:
            text =driver.find_element_by_xpath("//input[@value=' 确定 ']/../preceding-sibling::div[1]").text
            if "温馨提示" in text:
                driver.find_element_by_css_selector("input[value=' 确定 ']").click()
                break
            else:
                result.append(["失败",text,phone])
                driver.find_element_by_css_selector("input[value=' 确定 ']").click()
                js="window.scrollTo(0,0)"
                driver.execute_script(js)
                time.sleep(1)
                return driver
        except Exception as e:
            pass
    time.sleep(1)
    driver.switch_to_frame('feeframe')
    driver.find_element_by_id('continueTrade').click()

    time.sleep(1)
    while(1):
        try:
            driver.find_element_by_css_selector("input[value=' 确定 ']").click()
        except Exception as e:
            break
    time.sleep(3)
    while(1):
        try:
            driver.switch_to.alert().dismiss()
        except Exception as e:
            break
    result.append(["成功","",phone])
    print ("success")
    return driver


if __name__ == "__main__":
    phones, peoples, tcs= read.read("D:/自动受理数据.xlsx")
    driver= webdriver.Ie()
    driver.get('http://cbss.10010.com/')
    driver = login(driver)
    driver = nav0(driver)
    taocan = input('请输入套餐类型（108/138/218/238/258/98等）')
    tc=str(taocan)
    total = len(phones)
    for i in range(1,total):
        try:
            if taocan=="auto":
                driver = nav1(driver,tcs[i],phones[i],peoples[i])
            else:
                driver = nav1(driver,tc,phones[i],peoples[i])
            now = len(result)
            print (now)
            print (result[now-1])
        except Exception as e:
            for r in result:
                print (r)
            read.write(result)
            print (e)
            print (phones[i])
            input('wait')
    for r in result:
        print (r)
    read.write(result)
    input('finished')

    driver.quit()
