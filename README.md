# Python Turbo Warrant Stop-Loss Calculator

![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white)

> **Project Context:** This tool was developed in parallel with my studies over a one-week period in 2024 when I started trading turbos on my own. While straightforward in design, the primary goal of this tool was to automate repetitive calculations and eliminate manual errors

## Description
This simple code, developed in Python, is designed for traders to improve their risk management when investing in Turbo warrants.

The script precisely calculates the **stop-loss price** for a Turbo (Call or Put) based on three key inputs:
1. The initial investment amount.
2. The Turbo's purchase price.
3. The user's maximum acceptable monetary loss (€).

By determining the exact exit price, this tool empowers traders to automate their risk calculations and enforce strict capital protection rules.

## Key Features

* **Risk Management:** Calculates the stop-loss price needed to respect a fixed maximum loss.
* **Helper Function:** Includes an optional helper function to calculate the Turbo's initial price based on the underlying asset, strike, and parity.
* **Robust Validation:** Features robust input validation to ensure data integrity and prevent calculation errors.
