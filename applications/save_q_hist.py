#!/usr/bin/python
# Copyright (c) 2018 Warren Usui, MIT License
"""
Save question history for all players
"""
from save_user_hist import save_user_hist
from llama_slobber import get_qhist

if __name__ == "__main__":
    save_user_hist(get_qhist, 'question_data')
