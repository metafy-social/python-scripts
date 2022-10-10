## Check-System-Usage

![built by developers](http://ForTheBadge.com/images/badges/built-by-developers.svg)
![python](https://img.shields.io/badge/language-Python-orange?style=for-the-badge)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg?style=plasitc)](https://github.com/psf/black)
![License](https://img.shields.io/github/license/GDSC-RCCIIT/General-Purpose-Scripts?color=blue&style=plasitc)

### About

A Python3 script to send your desired payload to PagerDuty and create an incident


### Steps

 * Make sure you have create a serive in your PagerDuty account. [Refer here](https://support.pagerduty.com/docs/services-and-integrations) if not done already
 * Copy the Integration Key from the settings of the service as shown below and paste it in your env file
 <img width="1344" alt="Screenshot 2022-10-11 at 12 09 33 AM" src="https://user-images.githubusercontent.com/10003129/194933099-13dd03b8-c139-4366-bf18-272fd2ae7392.png">
 
 * Import the file as a module
 * Send your desired payload to the module
 * My example of payload
    ```
    payload= {
    "resource_id" : resource_id,
    "system_data":"This a resource in the development system of XYZ corp.",
    "tags":"'HA System','Non-critical-system','SpringBoot-App'"
    ```
 * Finalize your payload accoring the parameters(severity,components etc .)
 * Voila! If everything works fine you will recieve a Page 
 
