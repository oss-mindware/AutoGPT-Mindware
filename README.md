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
![machine-learning](https://github.com/open-mindware/AutoGPT-Mindware/assets/23727727/6d982e1b-ffff-4fe5-9820-04441f8e77d2)

## 📚 Prerequisites

### 1. Obtain Mindware API Key

Sign up to [Mindware](https://mindware.xyz) and locate your free API key on the account page:

<img width="945" alt="Screenshot 2023-08-27 145759" src="https://github.com/open-mindware/AutoGPT-Mindware/assets/23727727/00583046-3468-4bfe-b32d-5a6c76009068">

### 2. Install the Plugin

To install the plugin, execute the following command in the root directory of Auto-GPT:

#### For Mac, Linux, or WSL:

```bash
cd plugins && git clone https://github.com/open-mindware/AutoGPT-Mindware.git && zip -r ./AutoGPT-Mindware.zip ./AutoGPT-Mindware && rm -rf ./AutoGPT-Mindware && cd .. && ./run.sh --install-plugin-deps
```

#### For Windows (Powershell):

```powershell
cd plugins; git clone https://github.com/open-mindware/AutoGPT-Mindware.git; Compress-Archive -Path .\\AutoGPT-Mindware -DestinationPath .\\AutoGPT-Mindware.zip; Remove-Item -Recurse -Force .\\AutoGPT-Mindware; cd ..
```

## 🔧 Configuration Steps

### 1. Update the `.env` File

Add your Mindware API key to your `.env` file by appending the following lines:

```env
################################################################################
### MINDWARE
################################################################################

MINDWARE_API_KEY=your_api_key_here
```

### 2. Create or update `plugins_config.yaml` File

If the `plugins_config.yaml` file doesn't exist, **create a one**. Then, add the following configuration:

```yaml
MindwarePlugin:
  config: {}
  enabled: true
```
### 3. Run Auto-GPT

#### For Mac, Linux, or WSL:

```bash
./run.sh --install-plugin-deps
```

#### For Windows (Powershell):

```powershell
.\run.bat --install-plugin-deps
```

#### Directly Via CLI:

```
python -m autogpt --install-plugin-deps
```

## 🧠 How to Use

After completing the installation and configuration steps, you can enable specific plugins for Auto-GPT via the [plugin portal](https://mindware.xyz). For instance, if you want Auto-GPT to find YouTube videos, enable the YouTube plugin:

<img width="945" alt="Screenshot 2023-08-27 151437" src="https://github.com/open-mindware/AutoGPT-Mindware/assets/23727727/bcdb83bd-36e3-4993-b6ac-83660ef1cc0d">

### Example:

#### 1. Configure Auto-GPT

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

#### 2. Run Auto-GPT

Launch Auto-GPT. It should utilize the YouTube plugin to find sushi videos 🍣

