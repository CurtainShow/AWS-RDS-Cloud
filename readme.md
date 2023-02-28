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
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]



<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/github_username/repo_name">
    <img src="documentation/src/Logo-RDS.png" alt="Logo" >
  </a>

<h3 align="center"> Intégration des données dans le Cloud Amazon </h3>

  <p align="center">
    <img src="documentation/src/project-steps.png" alt="Logo" >
    <br />
    <a href="https://github.com/github_username/repo_name"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/github_username/repo_name">View Demo</a>
    ·
    <a href="https://github.com/github_username/repo_name/issues">Report Bug</a>
    ·
    <a href="https://github.com/github_username/repo_name/issues">Request Feature</a>
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#aws-rds">AWS RDS</a></li>
    <li><a href="#aws-bucket">AWS BUCKET</a></li>
    <li><a href="#machine-learning">Machine Learning</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

### Built With

* ![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
* ![Pandas](https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white)
* 	![TensorFlow](https://img.shields.io/badge/TensorFlow-%23FF6F00.svg?style=for-the-badge&logo=TensorFlow&logoColor=white)
* ![AWS](https://img.shields.io/badge/AWS-%23FF9900.svg?style=for-the-badge&logo=amazon-aws&logoColor=white)
* ![MySQL](https://img.shields.io/badge/mysql-%2300f.svg?style=for-the-badge&logo=mysql&logoColor=white)


<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

This is an example of how you may give instructions on setting up your project locally.
To get a local copy up and running follow these simple example steps.

### Prerequisites

Prerequisites list of things you need to use the software and how to install them.
* Homebrew
  ```sh
  /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
  ```

* PyEnv
  ```sh
  brew install pyenv
  ```

* Python 3.9.5 (or greater)
  ```sh
  pyenv install 3.9.5 
  ```
  
* Streamlit (for the reporting file)
  ```sh
  pip install streamlit
  ```

### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/CurtainShow/AWS-RDS-Cloud
   ```
2. Install Packages (or run first cell in script)
   ```sh
   pip install pymysql
   pip install pandas
   pip install tqdm
   pip install tensorflow
   ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## Usage

<img src="documentation/screenshot/AWS-Project-final.png" alt="Logo" >

_For more examples, please refer to the [Documentation](https://example.com)_

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ROADMAP -->
## Roadmap

- [x] Search for the dataset that contains structured and unstructured data
- [x] Structured data flows to the cloud
- [x] Unstructured data flows to the cloud
- [x] Production of dashboards
- [x] Bonus : Testing an ML algorithm on the dataset

See the [open issues](https://github.com/github_username/repo_name/issues) for a full list of proposed features (and known issues).

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- AWS - RDS -->
## AWS RDS

1. **Create an RDS** instance on Amazon Web Service
2. **Create a database** on the RDS instance
3. **Connect the database** to Python (PyMySQL)
4. **Create a table** with a schema that fits the chosen dataset
5. Read your dataset with Pandas
6. **Feed the table** with your dataset

See the [full explanation](https://github.com/CurtainShow/AWS-RDS-Cloud/tree/main/script) in the Jupyter Notebook file.

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- AWS - BUCKET -->
## AWS BUCKET

1. **Create an S3** instance on Amazon Web Service
2. **Create a Bucket** on the S3 instance
3. **Feed the Bucket** with your unstructured files, picture in this case, thanks to the AWS command line 

### Commands used to feed the instance

* aws s3 mb s3://awsprojetesgi
* cd /Volumes/GoogleDrive/My\ Drive/ESGI/Deep\ Learning/dataset/original
* aws s3 sync . s3://awsprojetesgi 
* aws s3 ls s3://awsprojetesgi
* aws s3 rm s3://awsprojetesgi --recursive

See the [full explanation](https://github.com/CurtainShow/AWS-RDS-Cloud/tree/main/script) in the Jupyter Notebook file.

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- MACHINE LEARNING -->
## Machine Learning

1. **Import the libraries** used for the process (Tensorflow, Pandas, Numpy, etc...)
2. **Create a data frame** from your dataset (Pandas)
3. **Split your data** into two parts (Training 80%, Test 20%)
4. **Pre-process your data** frame to retrieve only the data you need (Review, Rating, Book-id, etc...)
5. **Tokenize** the review with a pre-trained ressource: **GloVE 6B 200d** (Analysis on text requires a vectorization of your information to be meaningful for the computer)
6. **Create your model** (Embedding, Conv1D,MaxPooling1D, Dropout, Flatten, Dense)
7. **Train your model** and adjust your hyper-parameters
8. **Predict your Test dataset**
9. **Render the result** on a CSV file

See the [full explanation](https://github.com/CurtainShow/AWS-RDS-Cloud/tree/main/documentation) in the Jupyter Notebook file.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTACT -->
## Contact

- Ellen Boes - [@EllenBoes](https://github.com/EllenBoes)
- Adrian Barqueros - [@brqan](https://github.com/brqan)
- Allan Barbot - [@Veekah](https://github.com/CurtainShow)

Project Link: [https://github.com/CurtainShow/AWS-RDS-Cloud](https://github.com/github_username/repo_name)

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

* [MySQL - Documentation](https://dev.mysql.com/doc/)
* [AWS RDS - Documentation](https://docs.aws.amazon.com/rds/index.html)
* [Tensorflow - Documentation](https://www.tensorflow.org/api_docs)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/CurtainShow/AWS-RDS-Cloud.svg?style=for-the-badge
[contributors-url]: https://github.com/CurtainShow/AWS-RDS-Cloud/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/CurtainShow/AWS-RDS-Cloud.svg?style=for-the-badge
[forks-url]: https://github.com/CurtainShow/AWS-RDS-Cloud/network/members
[stars-shield]: https://img.shields.io/github/stars/CurtainShow/AWS-RDS-Cloud.svg?style=for-the-badge
[stars-url]: https://github.com/CurtainShow/AWS-RDS-Cloud/stargazers
[issues-shield]: https://img.shields.io/github/issues/CurtainShow/AWS-RDS-Cloud.svg?style=for-the-badge
[issues-url]: https://github.com/CurtainShow/AWS-RDS-Cloud/issues
[license-shield]: https://img.shields.io/github/license/CurtainShow/AWS-RDS-Cloud.svg?style=for-the-badge
[license-url]: https://mit-license.org/
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://www.linkedin.com/in/allan-barbot-57a0a2164/
[product-screenshot]: images/screenshot.png
[Next.js]: https://img.shields.io/badge/next.js-000000?style=for-the-badge&logo=nextdotjs&logoColor=white
[Next-url]: https://nextjs.org/
[React.js]: https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB
[React-url]: https://reactjs.org/
[Vue.js]: https://img.shields.io/badge/Vue.js-35495E?style=for-the-badge&logo=vuedotjs&logoColor=4FC08D
[Vue-url]: https://vuejs.org/
[Angular.io]: https://img.shields.io/badge/Angular-DD0031?style=for-the-badge&logo=angular&logoColor=white
[Angular-url]: https://angular.io/
[Svelte.dev]: https://img.shields.io/badge/Svelte-4A4A55?style=for-the-badge&logo=svelte&logoColor=FF3E00
[Svelte-url]: https://svelte.dev/
[Laravel.com]: https://img.shields.io/badge/Laravel-FF2D20?style=for-the-badge&logo=laravel&logoColor=white
[Laravel-url]: https://laravel.com
[Bootstrap.com]: https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white
[Bootstrap-url]: https://getbootstrap.com
[JQuery.com]: https://img.shields.io/badge/jQuery-0769AD?style=for-the-badge&logo=jquery&logoColor=white
[JQuery-url]: https://jquery.com 
