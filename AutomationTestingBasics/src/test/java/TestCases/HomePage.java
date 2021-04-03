package TestCases;

import org.apache.logging.log4j.Logger;
import org.openqa.selenium.WebDriver;
import org.testng.annotations.AfterTest;
import org.testng.annotations.BeforeTest;
import org.testng.annotations.DataProvider;
import org.testng.annotations.Test;
import pageObjects.LandingPage;
import pageObjects.LoginPage;
import resources.base;
import org.apache.logging.log4j.LogManager;
import java.io.IOException;

public class HomePage extends base {
    public WebDriver driver;
    public static Logger log = LogManager.getLogger(base.class.getName());
    @BeforeTest
    public void init() throws IOException {
        log.info("Initialized driver");
        driver = initializeDriver();
    }

    @Test(dataProvider = "getData")
    public void basePageNavigation(String username, String password) {
        driver.get(prop.getProperty("url"));
        LandingPage home = new LandingPage(driver);
        LoginPage login = home.getSignin();
        login.getEmail().sendKeys(username);
        login.getPassword().sendKeys(password);
        login.getLoginButton().click();
        log.info("Validated Home");
    }

    @AfterTest
    public void close() {
        driver.quit();
    }

    // The test will run 2 times to check both combinations
    @DataProvider
    public Object[][] getData(){
        Object[][] data = new Object[3][2];
        data[0][0] = "test@gmail.com";
        data[0][1] = "password123";
        data[1][0] = "test2@gamil.com";
        data[1][1] = "password324";
        data[2][0] = "test3@gmail.com";
        data[2][1] = "password1234";
        return data;
    }
}
