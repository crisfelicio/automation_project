from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

class DemoPage:
    def __init__(self, driver): 
        self.driver = driver

    def get_first_log(self):
      return self.driver.find_element(By.CSS_SELECTOR, ".py-p:nth-child(1)").text

    def subscribe_to_discipline_tmp(self, discipline_id):
      self.driver.find_element(By.ID, "subscribe-discipline-id").click()
      self.driver.find_element(By.ID, "subscribe-discipline-id").send_keys(discipline_id)
      self.driver.find_element(By.CSS_SELECTOR, ".form-group:nth-child(6) > #course-btn").click()

    def subscribe_student_to_discipline(self):
      self.driver.find_element(By.ID, "subscribe-student-id").click()
      self.driver.find_element(By.ID, "subscribe-student-id").send_keys("1")
      self.driver.find_element(By.ID, "subscribe-discipline-id").click()
      self.driver.find_element(By.ID, "subscribe-discipline-id").send_keys("1")
      self.driver.find_element(By.CSS_SELECTOR, ".form-group:nth-child(6) > #course-btn").click()

    def add_discipline_tmp(self, discipline):
      self.driver.find_element(By.ID, "discipline-nome").click()
      self.driver.find_element(By.ID, "discipline-nome").send_keys(discipline)
      self.driver.find_element(By.CSS_SELECTOR, ".form-group:nth-child(5) > #course-btn").click()

    def add_course_tmp(self, course):
      self.driver.find_element(By.ID, "course-nome").click()
      element = self.driver.find_element(By.ID, "course-nome")
      actions = ActionChains(self.driver)
      actions.double_click(element).perform()
      self.driver.find_element(By.ID, "course-nome").send_keys(course)
      self.driver.find_element(By.ID, "course-btn").click()

    def subscribe_discipline_to_course(self):
      self.driver.find_element(By.ID, "discipline-nome").click()
      self.driver.find_element(By.ID, "discipline-nome").send_keys("mat")
      self.driver.find_element(By.ID, "course-discipline-id").click()
      self.driver.find_element(By.ID, "course-discipline-id").send_keys("1")
      self.driver.find_element(By.CSS_SELECTOR, ".form-group:nth-child(5) > #course-btn").click()

    def add_student_to_course(self):
      self.driver.find_element(By.ID, "student-id").click()
      self.driver.find_element(By.ID, "student-id").send_keys("1")
      self.driver.find_element(By.ID, "course-id").click()
      self.driver.find_element(By.ID, "course-id").send_keys("1")
      self.driver.find_element(By.CSS_SELECTOR, ".form-group:nth-child(4) > #course-btn").click()

    def add_course(self):
      self.driver.find_element(By.ID, "course-nome").click()
      self.driver.find_element(By.ID, "course-nome").send_keys("mat")
      self.driver.find_element(By.ID, "course-btn").click()

    def add_student(self, student):
      self.driver.find_element(By.ID, "student-nome").click()
      self.driver.find_element(By.ID, "student-nome").send_keys(student)
      self.driver.find_element(By.ID, "student-btn").click()

    def wait_page_load(self):
      elements = self.driver.find_elements(By.CSS_SELECTOR, ".smooth")        
      while len(elements) > 0:
        elements = self.driver.find_elements(By.CSS_SELECTOR, ".smooth")            
        time.sleep(0.5)