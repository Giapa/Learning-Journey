package TestCases;

import org.apache.logging.log4j.LogManager;
import org.apache.logging.log4j.Logger;
import org.openqa.selenium.WebDriver;
import org.testng.Assert;
import org.testng.annotations.AfterTest;
import org.testng.annotations.BeforeTest;
import org.testng.annotations.Test;
import pageObjects.LandingPage;
import resources.base;

import java.io.IOException;

public class ValidateTitle extends base {
    public static Logger log = LogManager.getLogger(base.class.getName());
    public WebDriver driver;

    @BeforeTest
    public void init() throws IOException {
        driver = initializeDriver();
        log.info("Initialized driver");
        driver.get(prop.getProperty("url"));
    }

    @Test()
    public void basePageNavigation() {
        LandingPage home = new LandingPage(driver);
        Assert.assertEquals(home.getTitle().getText(), "FEATURED COURSESw");
        log.info("Validated Title");
    }

    @AfterTest
    public void close() {
        driver.quit();
    }
}
