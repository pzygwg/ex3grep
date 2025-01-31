# Vulnerable E-commerce Application

This is a deliberately vulnerable Flask application that demonstrates the limitations of SAST tools and the effectiveness of DAST tools in finding business logic vulnerabilities.

## Vulnerability Description

The application contains a price manipulation vulnerability in its purchase flow. The price is sent from the client side and is not validated against the server-side price, allowing attackers to modify the price parameter and make purchases at arbitrary prices.

## Setup

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Run the application:
```bash
python app.py
```

3. Access the application at http://localhost:5000

## Testing the Vulnerability

### SAST Testing (Semgrep)

Run Semgrep to demonstrate that it cannot detect this business logic vulnerability:

```bash
semgrep --config auto
```

### DAST Testing (Burp Suite/OWASP ZAP)

1. Configure your browser to use Burp Suite/ZAP as a proxy
2. Browse to http://localhost:5000
3. Try to purchase a product
4. Intercept the POST request to /purchase
5. Modify the 'price' parameter to a lower value
6. Observe that the server accepts the modified price

## Security Impact

This vulnerability allows attackers to:
- Purchase products at arbitrary prices
- Potentially cause financial loss to the business
- Bypass intended business logic controls

## Why SAST Tools Miss This

SAST tools like Semgrep analyze code statically and look for known vulnerable patterns. They cannot detect:
- Missing server-side validation
- Runtime data flow issues
- Complex business logic flaws

This demonstrates why both SAST and DAST tools are necessary for comprehensive security testing.