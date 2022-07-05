# import webdriver
path = "chromedriver path"
driver = webdriver.chrome(path)
driver.get("")
# driver.close() closes current tab, driver.quit() closes the entire browser
main = driver.find_element(By.ID, "idTest")
articles = driver.find_elements(By.TAG_NAME, "article")
for article in articles:
    header = driver.find_element(By.class_Name, 'className')
    print(header.text)
# Need to make sure elements exist on the page before clicking and continuing
# driver.back() lets you go back to the previous page, super fast because the page is already cached
# driver.forward() lets you go forward in your page history
# action chains are potent because they let you setup a series of actions which can be queued up to run consecutively after
# can store your actions then run a .perform() method on the actions object to perform all the actions in sequence
# very useful to use actionchains when you want to perform a few different sets of actions. set them up in that object then perform then whenever
# Putting the upgrades through a list so they can see which ones they can upgrade
item = [driver.find_element(By.ID, "productName" + str(i)) for i in range(1, -1, -1)]
# finds all the elements with the productName ID with a number attached to the end of it but starts with the larger number so the more expensive items are upgraded first (this is why it's not zero indexed)
actions.click(cookie)

# max amount of times you'd like to run the for loop
for i in range(5000):
    actions.perform()
    count = int(cookie_count.text.split(" ")[0])
    # Taking the first value before the space then converting it to an int
    for item in items:
        value = int(item.text)
        # so you have enough cookies to afford it, purchase the item
        if value <= count:
            upgrade_actions = ActionChains(driver)
            # move the cursor to the item element
            upgrade_actions.move_to_element(item)
            # press the cursor down
            upgrade_actions.click()
            upgrade_actions.perform()
            # This action chain is defined within the scope of this loop because we have different items within a list and don't know which item it's going to be
            # For this reason, you need to redefine the action chain every time to make sure you go to the correct item