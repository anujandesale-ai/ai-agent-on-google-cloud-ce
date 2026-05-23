## Steps to deploy AI application on GCP instance
1. Go to the google console. 
2. Search for compute engine
3. Create an Instance with machine type n1-standard-4 machine  
4. Ssh in the instance nd install git and python in the VM
   <br>4.1 Check OS version => ```cat /etc/os-release```
   <br>4.2 Updage package manager => ```sudo apt update```
   <br>4.3 Install git => ```sudo apt install -y git```
   <br>4.4 check git version => ```git -v```
   <br>4.5 Install python => ```sudo apt install -y python3.11```
   <br>4.6  ```python3 -v```
5. You are on path ```/home/anujadesale```
6. Create workspace => ```mkdir ai-space```
7. Clone git repo => ```git clone https://huggingface.co/spaces/voldemortuk/healthsense-main-new```
8. ```cd healthsense-main-new/```
9. create virtual env => ```python3 -m venv deploy_genai_venv```
   <br>9.1 if venv is not present, then install it => ```sudo apt install python3.11-venv```
   <br>9.2 if pip is not present , then install it => ```sudo apt install python3-pip```
10. Activate the env => ```source deploy_genai_venv/bin/activate```
11. Install all dependencies => ```pip install -r requirements.txt```
12. Edit file to update openai api key => ```vi constants.py```
13. Edit app.py to update CREWAI_STORAGE_PATH => ```vi app.py```
14. Test if env is loaded with success => ```python3 test_env.py```
15. Finally start application => ```python3 ./src/app.py```
16. The application will be successfully started on ```0.0.0.0/0:7860``` port.
17. To enable incoming traffic on 7860, add firewall rule

## Steps to add firewall rule (Open the Necessary Port (Firewall Rule))
1. In the Google Cloud Console search bar, type "Firewall" and select "Firewall"
2. Click "Create Firewall Rule".
3. Name: ```allow-app-access```
4. Network: ```default```
5. Direction of traffic: ```Ingress```
6. Action on match: ```Allow```
7. Targets: ```All instances in the network```
8. Source filter: ```IPv4 ranges```
9. Source IPv4 ranges: ```0.0.0.0/0``` (This allows traffic from anywhere).
10. Protocols and ports: Check "Specified protocols and ports", then check "tcp" and enter the port your application is using ```7860```.
11. Click Create.

## Access the application histed on gcp instance
Once the firewall rule is active. 
Open your browser.
Type ```http://YOUR_EXTERNAL_IP:7860```
Example: [http://34.123.45.67:8080](http://34.123.45.67:8080)
It should launch the application with success.
