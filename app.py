import json
from flask import Flask, request, render_template, session,flash,url_for,redirect
import jsonify
import databaseFunctions
import re
from importlib import reload
import requests
