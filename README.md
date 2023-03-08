
# Setup Process:
Required Dependencies:
    python (https://www.python.org/downloads/)
    docker (https://docs.docker.com/get-docker/)
    docker-compose (likely included with docker desktop, but if not: https://docs.docker.com/compose/)
    awscli: pip install awscli
    awscli-local: pip install awscli-local
    postgres SQL (be sure it is running on port 5432): https://www.postgresql.org/download/

# Running the application:
Configure Venv:
    Suggested environment:
        Use VSCode to create a new venv, using this guide: https://code.visualstudio.com/docs/python/environments
        This will automatically set up a venv with the requirements in requirements.txt

    Alternative method:
        Run the following commands to manually set up the venv:
            - pip install virtualenv
            - virtualenv venv to create your new environment
            - source venv/bin/activate
            - pip install -r requirements.txt

Run docker-compose.yml:
    Execute the following command to start the docker containers:
        - docker-compose up
    To take down the containers and rebuild from scratch:
        - docker-compose down && docker-compose build --no-cache && docker-compose up

Run app.py
    Once the venv and containers are setup, you should be able to run the application with this command (from the root of this repository):
        - py app.py (Windows)
        - python app.py (Mac OS)

View Results:
    Once the app.py file runs, viewing the records in the table should be as easy as running the following 2 commands:
        - psql -d postgres -U postgres -p 5432 -h localhost -W
        
        Password: postgres
        
        - postgres=# select * from user_logins;





# Prompts:
● How would you deploy this application in production?
    - As a standalone App, this seems like a good fit for a serverless Lambda function.
● What other components would you want to add to make this production ready?
    - For any deployment, the best practice is to set up an automated CI/CD pipeline.
    - For automated deployments, I could use ECS ComposeX.
    - I would also set up unit tests for the project which would run as part of the pipeline.
    - Environment variables in '.env' would need to be replaced with appropriate production or staging variables. And, not stored/exposed in the repository as this is a security risk.
    - Finally, we'd likely need to provision the correct permissions to the serverless lambda function so that it could access the SQS queue.
● How can this application scale with a growing dataset?
    - Currently we just mock the sqs data with a localstack container. But in production, records would constantly be getting added to the queue and need to be loaded to the table.
    - As such, we would likely want to turn this application into some sort of trigger-able API that was capable of processing new queue entries on demand.
    - Also, I would likely be pushing the data into a database hosted on AWS, such as Amazon RDS, instead of a container.
● How can PII be recovered later on?
    - My 'encryption' algorithm is very simple - it just reverses the strings to mask them. So, to recover the original values the analysts would just reverse the masked string.
    - Of course, if this were actual sensitive information, we would likely need to look into a more complicated approach with a shared encryption key and an encryption python library.
● What are the assumptions you made?
    - Amount of data:
        - I only loaded 10 records from the SQS localstack container to the psql table as a proof-of-concept. In production, we'd be storing a lot more than that.
        - For 'production' I'd also need to delete the sqs records that had been read so that they weren't picked up again.
    - Encryption:
        - As previously mentioned, I stuck with a simple string reversal to encrypt the sensitive information. In reality, we'd need to look into a more secure method of doing this, likely with a python encryption library.
    - Fault tolerance:
        - For brevity, I didn't spend time validating the data for cases that could crash the application (checking NoneType exceptions, etc.). But in production we'd obviously want to have strong fault tolerance.

