package StepDefinition;

import io.cucumber.java.en.Given;
import io.cucumber.java.en.Then;
import io.cucumber.java.en.When;
import io.cucumber.junit.Cucumber;
import org.junit.runner.RunWith;
import org.openqa.selenium.WebDriver;
import org.testng.Assert;
import pageObjects.LandingPage;
import pageObjects.LoginPage;
import pageObjects.PortalHomePage;
import resources.base;

import java.io.IOException;

//@RunWith(Cucumber.class) only when using junit
public class StepDefinition extends base {
    WebDriver driver;
    LandingPage home;
    LoginPage login;

    @Given("^Initialize the browser with chrome$")
    public void initialize_the_browser_with_chrome() throws IOException {
        driver = initializeDriver();
    }

    @When("^Navigate to \"([^\"]*)\" site$")
    public void navigate_to_something_site(String pageName) {
        String url = "http://www." + pageName + ".com";
        driver.get(url);

    }

    @Then("^Click on Login link in home page$")
    public void click_on_login_link_in_home_page() {
        home = new LandingPage(driver);
        if(home.getPopUpSize() > 0) {
            home.getPopUp().click();
        }
    }

    @When("^User enters (.+) and (.+) and logs in$")
    public void user_enters_something_and_something_and_logs_in(String username, String password) {
        login = home.getSignin();
        login.getEmail().sendKeys(username);
        login.getPassword().sendKeys(password);
        login.getLoginButton().click();
    }


    @Then("^Verify if user is successfully logged in$")
    public void verify_if_user_is_successfully_logged_in() {
        PortalHomePage portal = new PortalHomePage(driver);
        boolean flag = portal.getSearchBox().isDisplayed();
        Assert.assertTrue(flag);
    }

}