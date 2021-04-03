package pageObjects;

import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;

import java.util.List;

public class LandingPage {
    public WebDriver driver;
    private By signin = By.cssSelector("a[href*='sign_in']");
    //FindBy(css = "a[href*='sign_in']")
    //private WebElement signin;
    private By title = By.cssSelector("div[class='text-center'] h2");
    private By navbar = By.cssSelector(".nav.navbar-nav.navbar-right>li>a");
    private By popup = By.xpath("//button[text()='NO THANKS']");

    public LandingPage(WebDriver driver) {
        this.driver = driver;
    }

    // Return the new redirected page
    public LoginPage getSignin() {
        driver.findElement(signin).click();
        return new LoginPage(driver);
        //return signin;
    }

    public WebElement getTitle() {
        return driver.findElement(title);
    }

    public WebElement getNavbar() {
        return driver.findElement(navbar);
    }
    public int getPopUpSize(){
        return driver.findElements(popup).size();
    }
    public WebElement getPopUp(){
        return driver.findElement(popup);
    }
}
