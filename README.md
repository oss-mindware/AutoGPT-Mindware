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
<br />
<div align="center">
    <img src="https://wlqmlsriumpfpcnpgpxn.supabase.co/storage/v1/object/public/media/logos/mindware.png" alt="Logo" width="200" height="200">
</div>

## 📚 Prerequisites

### 1. Obtain Mindware API Key

Sign up for a [free Mindware account](https://mindware.xyz) to get your API key.

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

## 🚀 How to Use

After completing the installation and configuration steps, you can enable specific plugins for Auto-GPT via the [Mindware website](https://mindware.xyz). For instance, if you want to allow Auto-GPT to find YouTube videos, enable the YouTube plugin:

<img width="946" alt="Screenshot 2023-08-26 191713" src="https://github.com/open-mindware/AutoGPT-Mindware/assets/23727727/65c04ad1-a842-4342-8b28-802b966d91ef">

### Example:

#### 1. Configure Auto-GPT

Set up the `ai_settings.yaml` file with the following parameters:

```yaml
ai_goals:
  - Find YouTube videos on how to make salmon nigiri.
ai_name: FoodTubeGPT
ai_role:
  An AI-powered virtual assistant that specializes in helping users find and
  obtain specific cooking videos on YouTube.
api_budget: 0.05
```

#### 2. Run Auto-GPT

Launch Auto-GPT. It should utilize the YouTube plugin to find the specified content.
