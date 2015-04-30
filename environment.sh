#!/bin/bash
#export SETTINGS="config.DevelopmentConfig"

export SETTINGS='development'
export APPLICATION_SECRET_KEY='thisshouldbearandomvalue'
export SQLALCHEMY_DATABASE_URI='postgresql://trill:@0.0.0.0:5432/trill'
