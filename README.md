1. Go to the google console. 
2. Search for compute engine
3. Create an Instance with machine type n1-standard-4 machine  
4. Ssh in the instance nd install git and python in the VM
   4.1 Check OS version => cat /etc/os-release
   4.2 Updage package manager => sudo apt update
   4.3 Install git => sudo apt install -y git
   4.4 check git version => git -v
   4.5 Install python => sudo apt install -y python3.11
   4.6  python3 -v
5. You are on path /home/anujadesale
6. Create workspace => mkdir ai-space
7. Clone git repo => git clone https://huggingface.co/spaces/voldemortuk/healthsense-main-new
8. cd healthsense-main-new/
9. create virtual env => python3 -m venv deploy_genai_venv
   9.1 if venv is not present, then install it => sudo apt install python3.11-venv
   9.2 if pip is not present , then install it => sudo apt install python3-pip
10. Activate the env => source deploy_genai_venv/bin/activate
11. Install all dependencies => pip install -r requirements.txt
12. Edit file to update openai api key => vi constants.py
13. Edit app.py to update CREWAI_STORAGE_PATH => vi app.py
14. Test if env is loaded with success => python3 test_env.py
