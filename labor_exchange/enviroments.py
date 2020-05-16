from datetime import timezone as tz
from typing import List

from pydantic import BaseSettings, Field


__all__ = [
    'DjangoSettings',
    'DatabaseSettings',
    'LoggingSettings',
]


class _SettingsConfigureModel(BaseSettings):
    class Config:
        allow_mutation = False


class DjangoSettings(_SettingsConfigureModel):
    allowed_hosts: List[str] = Field(default='', env='allowed_hosts')
    debug: bool = Field(default=False, env='app_debug')
    secret_key: str = Field(..., env='secret_key')
    static_host: str = Field(default='', env='static_host')
    timezone: tz = tz.utc


class DatabaseSettings(_SettingsConfigureModel):
    host: str = Field(..., env='db_host')
    username: str = Field(..., env='db_username')
    password: str = Field(..., env='db_password')
    db_name: str = Field(..., env='db_name')
    port: int = Field(default='5432', env='db_port')

    @property
    def postgresql_url(self) -> str:
        return f'postgresql://{self.username}:{self.password}@{self.host}:{self.port}/{self.db_name}'


class LoggingSettings(_SettingsConfigureModel):
    pass
