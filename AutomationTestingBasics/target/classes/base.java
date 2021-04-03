package resources;
import org.apache.commons.io.FileUtils;
import org.openqa.selenium.OutputType;
import org.openqa.selenium.TakesScreenshot;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.chrome.ChromeOptions;
import org.openqa.selenium.firefox.FirefoxDriver;
import org.openqa.selenium.firefox.FirefoxOptions;

import java.io.File;
import java.io.FileInputStream;
import java.io.IOException;
import java.util.Properties;
import java.util.concurrent.TimeUnit;

public class base {
    public WebDriver driver;
    public Properties prop;

    public WebDriver initializeDriver() throws IOException {
        prop = new Properties();
        String propertyPath = System.getProperty("user.dir") + "/src/main/java/resources/data.properties";
        FileInputStream file = new FileInputStream(propertyPath);
        prop.load(file);
        String browser = prop.getProperty("browser");
        //String browser = System.getProperty("browser");
        if (browser.contains("chrome")) {
            ChromeOptions options = new ChromeOptions();
            if(browser.contains("headless")){
                options.addArguments("--headless");
            }
            driver = new ChromeDriver(options);
        } else if (browser.contains("firefox")) {
            FirefoxOptions options = new FirefoxOptions();
            if(browser.contains("headless")){
                options.addArguments("--headless");
            }
            driver = new FirefoxDriver();
        }
        driver.manage().timeouts().implicitlyWait(9000, TimeUnit.MILLISECONDS);
        return driver;
    }

    public String getScreenshotPath(String testCaseName, WebDriver driver) throws IOException {
        TakesScreenshot ts = (TakesScreenshot) driver;
        File src = ts.getScreenshotAs(OutputType.FILE);
        String path = System.getProperty("user.dir") + "/reports/" + testCaseName + ".png";
        FileUtils.copyFile(src, new File(path));
        return path;
    }
}
