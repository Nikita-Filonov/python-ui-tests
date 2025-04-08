# Python UI tests

## Links

- [Allure Report on GitHub Pages](https://nikita-filonov.github.io/python-ui-tests/13/index.html)
- [GitHub Actions CI/CD](https://github.com/Nikita-Filonov/python-ui-tests/actions)
- [UI Course Application](https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login) – The web
  application being tested
- [UI Course Repository](https://github.com/Nikita-Filonov/qa-automation-engineer-ui-course) – Source code for the UI
  Course

## Overview

This project provides an example of UI testing for a web application from
the [UI Course](https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login) using Python and
Playwright. The project demonstrates the usage of key technologies, design patterns, and best practices to ensure
efficient, maintainable, and readable UI tests. Key features of this project include:

- [Playwright](https://playwright.dev/python/) – A powerful browser automation tool for end-to-end testing.
- [Pytest](https://docs.pytest.org/en/stable/) – A full-featured testing framework for Python.
- [Allure](https://allurereport.org/) – A comprehensive test reporting framework that provides detailed and visually
  appealing reports.
- [PageObject](./pages) – To separate test logic from page-specific interaction logic, ensuring maintainable and
  scalable tests.
- [PageComponent](./components) – A custom pattern for abstracting and handling individual page components. This ensures
  better modularity and reusability, improving the maintainability of the test code.
- [PageFactory](./elements) – For creating and organizing page components dynamically and abstracting page details.
- [Fixtures](./fixtures) – For reusable setup and teardown logic.
- Logging and step-by-step reporting – Using custom loggers and Allure steps for better traceability.

The UI tests in this project cover key user journeys, such as user registration, and validate the presence and
functionality of various page elements.

## Setup Instructions

### Prerequisites

Ensure that you have the following installed on your system:

- Python 3.11 or later
- pip (Python package manager)
- Git

## Installation

Clone the repository and navigate to the project directory:

```shell
git clone https://github.com/Nikita-Filonov/python-ui-tests.git
cd python-ui-tests
```

Create and activate a virtual environment:

```shell
python -m venv venv # Create virtual environment
source venv/bin/activate # Activate on macOS/Linux
venv\Scripts\activate # Activate on Windows
```

Install dependencies:

```shell
pip install --upgrade pip # Upgrade pip to the latest version
pip install -r requirements.txt # Install required dependencies
playwright install # Install playwright dependencies
```

## Running Tests

To run UI tests using pytest:

```shell
pytest -m regression --numprocesses 2 # Run regression tests in parallel
```

## Generating Allure Reports

Run tests and generate Allure results:

```shell
pytest -m regression --alluredir=allure-results
```

To serve the Allure report locally:

```shell
allure serve allure-results
```

## Running Tests in CI/CD

Tests are automatically executed in a CI/CD pipeline using [GitHub Actions](https://github.com/features/actions). The
workflow is configured to:

- Run tests on every push and pull request to the main branch.
- Generate and upload Allure reports as artifacts.
- Publish the [Allure report](https://allurereport.org/) to [GitHub Pages](https://pages.github.com/) for easy access.

Ensure that the [gh-pages](https://github.com/Nikita-Filonov/python-ui-tests/tree/gh-pages) branch exists in your
repository for successful deployment. If it does not exist, create it manually:

```shell
git checkout --orphan gh-pages
```

Then push the new branch:

```shell
git push origin gh-pages
```

To allow GitHub Actions to publish the report, enable Workflow permissions:

- Open your repository on GitHub.
- Go to Settings > Actions > General.
- Scroll down to Workflow permissions.
- Select Read and write permissions.
- Click Save.

Once set up, your tests will run automatically, and the Allure report will be deployed to GitHub Pages.

## Accessing Allure Reports

After a successful test run in CI/CD:

- The Allure report will be available at [GitHub Pages](https://nikita-filonov.github.io/python-ui-tests/13/index.html).
- The workflow logs and artifacts can be accessed
  via [GitHub Actions](https://github.com/Nikita-Filonov/python-ui-tests/actions).
- If the [*pages build and deployment*](https://github.com/Nikita-Filonov/python-ui-tests/actions/runs/14263348460)
  workflow does not appear, verify your GitHub Pages settings:
    - Go to Settings > Pages.
    - Under Build and deployment, ensure the source is set to the `gh-pages` branch.

## Documentation for Used Actions

For detailed information on GitHub Actions used in this project, refer to the following:

- [Checkout Action](https://github.com/actions/checkout)
- [Setup Python Action](https://github.com/actions/setup-python)
- [Upload Artifact Action](https://github.com/actions/upload-artifact)
- [Download Artifact Action](https://github.com/actions/download-artifact)
- [Allure Report Action](https://github.com/simple-elf/allure-report-action)
- [GitHub Pages Deployment Action](https://github.com/peaceiris/actions-gh-pages)

## Summary

This project serves as a reference implementation for writing clean, maintainable, and effective UI tests in Python
using Playwright. It showcases best practices such as using the Page Object and Page Factory patterns, structured
logging, and Allure reporting. The setup allows for easy test execution locally and in CI/CD environments, ensuring
high-quality automated testing with minimal manual intervention.

