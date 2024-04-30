from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    """This will validate our environment variables.
    That are used to store valuable sensitive data.

    This also allows us to access the environment
    variables of our system."""

    database_hostname: str
    database_port: str 
    database_password: str
    database_name: str
    database_username: str
    secret_key: str
    algorithm: str
    access_token_expire_minutes: int


    class Config:
        env_file = '.env'

# creating an instance of the settings class
settings = Settings()