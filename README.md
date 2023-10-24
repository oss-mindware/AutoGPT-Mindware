<!-- Improved compatibility of back to top link: See: https://github.com/othneildrew/Best-README-Template/pull/73 -->

<a name="readme-top"></a>

<!--
*** Thanks for checking out the Best-README-Template. If you have a suggestion
*** that would make this better, please fork the repo and create a pull request
*** or simply open an issue with the tag "enhancement".
*** Don't forget to give the project a star!
*** Thanks again! Now go create something AMAZING! :D
-->

<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->

<!-- PROJECT LOGO -->
<div align="center">
    <img src="https://github.com/open-mindware/AutoGPT-Mindware/assets/23727727/6d982e1b-ffff-4fe5-9820-04441f8e77d2" alt="Logo" width="200" height="200">
</div>

## 📚 Prerequisites

### 1. OpenAI API Key

If you don't already have an OpenAI API key, get one [here](https://openai.com/blog/openai-api).

### 2. Mindware API Key

Sign up to [Mindware](https://mindware.xyz) and copy your free API key from the account page:

<img width="945" alt="Screenshot 2023-10-16 145320" src="https://github.com/open-mindware/AutoGPT-Mindware/assets/23727727/f7b72851-a613-4073-852e-c8d93ec2f1fe">


### 3. Docker Desktop

If you don't already have Docker inatalled, download the latest version [here](https://www.docker.com/products/docker-desktop).

## 🔧 Setup

### 1. Install AutoGPT & Mindware

To install AutoGPT and Mindware, make sure Docker is running and then run the following command in a directory of your choosing:

#### For Mac, Linux, or WSL:

```bash
git clone https://github.com/open-mindware/AutoGPT-Mindware-Installer.git && cd ./AutoGPT-Mindware-Installer && ./installer.sh
```

#### For Windows (Powershell):

```powershell
git clone https://github.com/open-mindware/AutoGPT-Mindware-Installer.git; .\AutoGPT-Mindware-Installer\installer.bat
```

### 2. Start AutoGPT

The last command will automatically start AutoGPT after the installation process. Whenever you want to start AutoGPT beyond then, run the following command from the AutoGPT directory:

```bash
docker compose run --rm auto-gpt --install-plugin-deps
```

## 🧠 How to Use

After completing these installation steps, you can enable/disable plugins for AutoGPT via the Mindware [plugins page](https://mindware.xyz). For instance, if you want AutoGPT to find YouTube videos, enable the YouTube plugin:

<img width="945" alt="Screenshot 2023-10-24 122112" src="https://github.com/open-mindware/AutoGPT-Mindware/assets/23727727/b47f991c-bd84-464c-88cc-c9163544b4a0">

### Example:

#### 1. Configure AutoGPT

Set up the `ai_settings.yaml` file with the following parameters:

```yaml
ai_goals:
  - Find YouTube videos on how to make Otoro nigiri.
ai_name: FoodTubeGPT
ai_role:
  An AI-powered virtual assistant that specializes in helping users find and
  obtain specific cooking videos on YouTube.
api_budget: 0.05
```

#### 2. Start AutoGPT

Launch AutoGPT. It should utilize the YouTube plugin to find sushi videos 🍣

