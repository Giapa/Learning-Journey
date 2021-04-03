package CucumberOptions;

import io.cucumber.junit.Cucumber;
//import io.cucumber.junit.CucumberOptions;
import io.cucumber.testng.CucumberOptions;
import io.cucumber.testng.AbstractTestNGCucumberTests;
import org.junit.runner.RunWith;

//@RunWith(Cucumber.class) when running with junit
@CucumberOptions(features = "src/test/java/Features",
        glue = "StepDefinition")
public class TestRunner extends AbstractTestNGCucumberTests {

}