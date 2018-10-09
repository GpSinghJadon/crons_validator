# crons_validator
This is a small module which will check weather the crons specified in the crontab are executing as per there configuration or not.

## Problem Statement :

## Proposed Solution :

## Requirements :
- Python 2.7 or higher
- Linux crontab

## Setup/Configuration :
First install all the required pip packages mentioned in the requirements.txt file.
```
pip install -r requirements.txt
```
There must be a valid crontab available in the system.

## Algorithm :
1. get the cron.tab path and user
2. read all the commands from the crontab
3. check if the command is correctly scheduled.
4. get the last modified time of the related log file.
5. get the previous runtime of the cron.
6. compare both the times, if the modified time of the file is greater than the previous runtime of the cron then the cron is properly set and if working fine.
7. else, there is an error which is to be reported.

## Built With

* [python-crontab](https://gitlab.com/doctormo/python-crontab) - The crontab parsing tool

## Contributing
Please suggest how can we make this more optimized

## Versioning

We use [github](https://github.com/) for versioning. For the versions available, see the [tags on this repository](https://github.com/GpSinghJadon/crons_validator). 

## Authors

* **Gajender Pal Singh** - *Initial work* - [MyOperator](https://github.com/GpSinghJadon)
## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Hat tip to anyone whose code was used
* Inspiration
* etc
