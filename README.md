<kbd style="width: 2em; height: 2em;"><a href="#en">ENGLISH</a></kbd> | <kbd><a href="#ru">РУССКИЙ</a></kbd>

<h1 name="en" id="en">Automatically Raise Your Resume on HH.RU!</h1>

A Python Selenium & GitHub Actions bot that automatically raises Your resume in the list on hh.ru

## GitHub Actions Contents

github.com/nakigoe/hh-ru-raise-bot/.github/workflows/raise.yml
```
name: Run Python Selenium headless script to raise a resume in the list on hh.ru

# Controls when the workflow will run
on:

  # Triggers the workflow on push or pull request events but only for the "main" branch
  schedule:
    - cron: '0 0 * * *'
    - cron: '5 4 * * *'
    - cron: '10 8 * * *'
    - cron: '15 12 * * *'
    - cron: '20 16 * * *'
    - cron: '25 20 * * *'
    - cron: "0 */4 * * *"

  # Allows you to run this workflow manually from the Actions tab
  workflow_dispatch:

# A workflow run is made up of one or more jobs that can run sequentially or in parallel
jobs:

  # This workflow contains a single job called "build"
  build:

    # The type of runner that the job will run on
    runs-on: ubuntu-latest

    # Steps represent a sequence of tasks that will be executed as part of the job
    steps:
      # Checks-out your repository under $GITHUB_WORKSPACE, so your job can access it
      - uses: actions/checkout@v3
      
      # Install Python
      - name: setup python
        uses: actions/setup-python@v3
        with:
          python-version: 3.x #install the python needed

      - name: execute py script # run the run.py to get the latest data
        run: |
          pip install --upgrade pip
          pip install selenium
      
      - name: Raise the resume
        run:
          python ./bot/raise.py
        env:
          LOGIN: ${{ secrets.LOGIN }}
          KEY: ${{ secrets.KEY }} 
```

## Usage
1) Clone the repository
2) Create Your own secret keys for GitHub Actions to login into HH.RU: LOGIN and KEY

<p>To quickly find <em>GitHub Actions Secrets</em> page, You can use the link:
<br> <em>github.com/<code>your-login</code>/<code>your-repository-name</code>/settings/secrets/actions/new</em>
<br> (change <code>your-login</code> and <code>your-repository-name</code>).</p>

![Create LOGIN and KEY Secrets for GitHub Actions](https://github.com/nakigoe/hh-ru-raise-bot/blob/main/github-secrets.png)

You have to create TWO keys, LOGIN и KEY, with the contents of Your login and password to hh.ru.


Everything is mission ready: Your resume will be raised every four hours on hh.ru automatically! 

Add stars to the pepositories!!! 

<hr>
<h1 name="ru" id="ru">HH.RU автоматическое поднятие резюме в списке каждые четыре часа</h1>

Бот на Python Selenium и GitHub Actions, автоматически поднимает Ваше резюме в списке на hh.ru

Всё настроено для использования бота на GitHub:
1) клонируйте репозиторий; 
2) создайте Ваши собственные ключи (secrets) уже Вашем репозитории в разделе GitHub Actions: LOGIN и KEY (Ваш логин и пароль к hh.ru) 

<p>Чтобы быстро найти страницу <em>создания нового секретного ключа GitHub Actions,</em> Вы можете перейти по сноске:
<br> <em>github.com/<code>ваш&#8209;ник</code>/<code>название&#8209;репозитория</code>/settings/secrets/actions/new</em>
<br> (внесите соответствующие изменения: <code>ваш ник</code> и <code>название репозитория</code>).</p>

![создание секретных ключей LOGIN и KEY для GitHub Actions](https://github.com/nakigoe/hh-ru-raise-bot/blob/main/github-secrets.png)

Вам необходимо создать ДВА ключа, LOGIN и KEY, содержание — Ваш логин и пароль к hh.ru.

Всё готово: бот запускается автоматически каждые четыре часа. Ставьте звёзды, пожалуйста!

<br> Пишите, если Вы хотите получить уроки создания вебсайтов: nakigoetenshi@gmail.com
<br> 1000 рублей 2 часа один урок

<h2 style="margin: 0 auto" align="center">Ставьте звёзды и делитесь сноской на репозиторий со всеми, кто искал работу, ищет работу, планирует искать работу!</h2>
<br>
<p style="margin: 0 auto" align="center">Посетите:</p>
<h1><a href="https://nakigoe.org/ru/" style="background-color: black;" target="_blank">
  <img style="display: block; width: calc(100vw - (100vw - 100%));"
    src="https://nakigoe.org/_IMG/logo.png" 
    srcset="https://nakigoe.org/_IMG/logo.png 4800w,
      https://nakigoe.org/_SRC/logo-3840.png 3840w,
      https://nakigoe.org/_SRC/logo-2560.png 2560w,
      https://nakigoe.org/_SRC/logo-2400.png 2400w,
      https://nakigoe.org/_SRC/logo-2048.png 2048w,
      https://nakigoe.org/_SRC/logo-1920.png 1920w,
      https://nakigoe.org/_SRC/logo-1600.png 1600w,
      https://nakigoe.org/_SRC/logo-1440.png 1440w,
      https://nakigoe.org/_SRC/logo-1280.png 1280w,
      https://nakigoe.org/_SRC/logo-1200.png 1200w,
      https://nakigoe.org/_SRC/logo-1080.png 1080w,
      https://nakigoe.org/_SRC/logo-960.png 960w,
      https://nakigoe.org/_SRC/logo-720.png 720w,
      https://nakigoe.org/_SRC/logo-600.png 600w,
      https://nakigoe.org/_SRC/logo-480.png 480w,
      https://nakigoe.org/_SRC/logo-300.png 300w"
    alt="NAKIGOE.ORG">
<img class="blend" style="display: block; width: calc(100vw - (100vw - 100%));" 
  src="https://nakigoe.org/_IMG/nakigoe-academy-night.jpg" 
  srcset="https://nakigoe.org/_IMG/nakigoe-academy-night.jpg 2800w,
    https://nakigoe.org/_SRC/nakigoe-academy-night-2048.jpg 2048w"
  alt="Nakigoe Academy">
  <img class="blend" style="display: block; width: calc(100vw - (100vw - 100%)); padding-bottom: 0.05em;"
    src="https://nakigoe.org/_IMG/logo-hot-bevel.png" 
    srcset="https://nakigoe.org/_IMG/logo-hot-bevel.jpg 4800w,
      https://nakigoe.org/_SRC/logo-hot-bevel-3840.jpg 3840w,
      https://nakigoe.org/_SRC/logo-hot-bevel-2560.jpg 2560w,
      https://nakigoe.org/_SRC/logo-hot-bevel-2400.jpg 2400w,
      https://nakigoe.org/_SRC/logo-hot-bevel-2048.jpg 2048w,
      https://nakigoe.org/_SRC/logo-hot-bevel-1920.jpg 1920w,
      https://nakigoe.org/_SRC/logo-hot-bevel-1600.jpg 1600w,
      https://nakigoe.org/_SRC/logo-hot-bevel-1440.jpg 1440w,
      https://nakigoe.org/_SRC/logo-hot-bevel-1280.jpg 1280w,
      https://nakigoe.org/_SRC/logo-hot-bevel-1200.jpg 1200w,
      https://nakigoe.org/_SRC/logo-hot-bevel-1080.jpg 1080w,
      https://nakigoe.org/_SRC/logo-hot-bevel-960.jpg 960w,
      https://nakigoe.org/_SRC/logo-hot-bevel-720.jpg 720w,
      https://nakigoe.org/_SRC/logo-hot-bevel-600.jpg 600w,
      https://nakigoe.org/_SRC/logo-hot-bevel-480.jpg 480w,
      https://nakigoe.org/_SRC/logo-hot-bevel-300.jpg 300w"
    alt="NAKIGOE.ORG">
</a></h1>
