#!/bin/bash

cd API
uvicorn cpa_api_reference:app --host "0.0.0.0" --port "8000"