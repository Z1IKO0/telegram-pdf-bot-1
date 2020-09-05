#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os

class Config(object):
  TELEGRAM_TOKEN = os.environ.get("TELEGRAM_TOKEN", "")
