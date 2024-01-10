Project parses **shop.kz** and returns smartphones with given price:
`GET /smartphones?price=xxxxxx`

short notice: first request gonna take some time as it will parse the website(19 pages) and consequent requests will load all the data from **smartphones.json** that we created after first request. 

## Quick start:

Get the code:

    $ git clone https://github.com/Tremos/Pre-Interview-Task.git

Build:

    $ cd Pre-Interview-Task
    $ docker-compose up --build

The application will be launched on `port 9000`. http://127.0.0.1:9000/