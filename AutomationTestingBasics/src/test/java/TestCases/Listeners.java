package TestCases;

import com.aventstack.extentreports.ExtentReports;
import com.aventstack.extentreports.ExtentTest;
import com.aventstack.extentreports.Status;
import org.openqa.selenium.WebDriver;
import org.testng.ITestContext;
import org.testng.ITestListener;
import org.testng.ITestResult;
import resources.ExtentReporter;
import resources.base;

public class Listeners extends base implements ITestListener {
    //For parallel run to make it thread safe
    ThreadLocal<ExtentTest> extentTest = new ThreadLocal<ExtentTest>();
    private ExtentReports extent = ExtentReporter.getReportObject();
    private ExtentTest test;

    @Override
    public void onTestStart(ITestResult iTestResult) {
        test = extent.createTest(iTestResult.getMethod().getMethodName());
        extentTest.set(test);
    }

    @Override
    public void onTestSuccess(ITestResult iTestResult) {
        extentTest.get().log(Status.PASS, "Test passed.");
    }

    @Override
    public void onTestFailure(ITestResult iTestResult) {
        String testCaseName = iTestResult.getMethod().getMethodName();
        try {
            WebDriver driver = (WebDriver) iTestResult.getTestClass().getRealClass().getDeclaredField("driver").get(iTestResult.getInstance());
            String path = getScreenshotPath(testCaseName, driver);
            extentTest.get().addScreenCaptureFromPath(path,testCaseName);
        } catch (Exception e) {
        }
        extentTest.get().fail(iTestResult.getThrowable());
    }

    @Override
    public void onTestSkipped(ITestResult iTestResult) {

    }

    @Override
    public void onTestFailedButWithinSuccessPercentage(ITestResult iTestResult) {

    }

    @Override
    public void onStart(ITestContext iTestContext) {

    }

    @Override
    public void onFinish(ITestContext iTestContext) {
        extent.flush();
    }
}
