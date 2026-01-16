This section presents an analysis of the credentials extracted during the intrusion test, focusing solely on enabled user accounts. Machine accounts and disabled users were therefore omitted.

As illustrated in the following figure, out of a total of **{{TOTAL_AMOUNT_OF_CREDS}}** credentials collected, **{{RECOVERED_AMOUNT_OF_CREDS}}** were successfully recovered through an offline password cracking process conducted over a 24-hour period. This represents a recovery rate of **{{RECOVERED_AMOUNT_OF_CREDS_PERCENTAGE}}**, highlighting a significant exposure of user credentials.

![Passwords Recovery Statistics](base64/imagedata)

A statistical analysis was subsequently performed on the complete set of obtained credentials to identify common password selection patterns among users. As shown in the following illustration, the most frequently observed password length was **{{HIGHEST_PASSWORD_LENGTH_DISTRIBUTION}}** characters, followed by **{{SECOND_HIGHEST_PASSWORD_LENGTH_DISTRIBUTION}}** characters. This distribution suggests a tendency toward predictable password lengths, which may facilitate password cracking attacks.

![Password Length Distribution](base64/imagedata)

Additionally, a password complexity assessment was carried out to evaluate compliance with a strong password policy. For the purpose of this analysis, a password was considered compliant if it met the following criteria:
- Minimum length of 8 characters
- Inclusion of at least 3 out of the following 4 character categories:
    - Uppercase letters (A–Z)
    - Lowercase letters (a–z)
    - Digits (0–9)
    - Special characters (!@#$%^&*…)

As depicted in the following figure, **{{COMPLIANCE_PASSWORD_PERCENTAGE}}** of the recovered credentials satisfied these requirements. Despite this, the fact that such passwords were still successfully recovered indicates a margin for improvement, particularly in areas such as password uniqueness, entropy, and resistance to common cracking techniques.

![Password Policy Compliance Statistics](base64/imagedata)

Finally, password reuse across the domain was evaluated. As shown in the following illustration, multiple accounts were identified as sharing identical passwords. This behavior significantly increases the impact of a single credential compromise and evidences a weak password hygiene policy, enabling lateral movement and privilege escalation within the environment.

![Top 10 Most Used Passwords](base64/imagedata)
