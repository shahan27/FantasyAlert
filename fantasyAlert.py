from lib2to3.pgen2.token import LEFTSHIFT
from pickle import NONE
from re import S, X
import tkinter as tk
from tkinter import BOTTOM, CENTER, E, LEFT, NE, RIGHT, TOP, W, ttk
from tkinter.messagebox import YES, showinfo
from turtle import left
from playsound import playsound
import tweepy
import os
import time
import cred

watchList = {}
# root window
root = tk.Tk()
root.title("Fantasy Alert Application")
root.geometry("900x600+50+50")
root.resizable(False, False)
root.configure(bg="orange")


# store email address and password
playerSearch = tk.StringVar()
watchlistAdd = tk.StringVar()

auth = tweepy.OAuthHandler(cred.OAhan, cred.OAhan2)
auth.set_access_token(
    cred.Authset,
    cred.AuthsetT,
)

api = tweepy.API(auth)


def login_clicked():
    """callback when the search button clicked"""
    msg = f"You entered a player called: {playerSearch.get()} and added to your watchlist: {watchlistAdd.get()}"
    playerReports(playerSearch.get())


def add_clicked():
    """add player to watch list"""
    msg = f"You entered a player called: {playerSearch.get()} and added to your watchlist: {watchlistAdd.get()}"
    showinfo(title="Information", message=msg)
    addWatchList(watchlistAdd.get())
    print(watchList)


def remove_clicked():
    """remove player to watch list"""
    msg = f"You entered a player called: {playerSearch.get()} was removed from your watchlist: {watchlistAdd.get()}"
    showinfo(title="Information", message=msg)
    removePlayer(watchlistAdd.get())


# add and remove from watchlist


def addWatchList(name):
    player = name
    watchList[player] = 0


def removePlayer(player):
    if player in watchList:
        watchList.pop(player)
    else:
        print("player is not in watch list")


def playerReports(name):
    for status in tweepy.Cursor(
        api.search,
        q="%s from:FantasyLabsNBA" % (name),
        rpp=5,
        show_user=True,
    ).items(1):
        reportLabel = ttk.Label(playerReportFrame, text=status.text)
        reportLabel.grid(sticky=tk.W)
        playsound("piano.wav")


# search frame
search = ttk.Frame(root)
search.pack(padx=10, pady=10, side=RIGHT, anchor=NE)

# watchlist frame
watchListFrame = ttk.Frame(root, width=700, height=250)
watchListFrame.pack(padx=10, pady=10, side=TOP, anchor=W)

# player report frame
playerReportFrame = ttk.Frame(root, width=7000, height=2500)
playerReportFrame.pack(padx=10, anchor=CENTER)


reportLabel = ttk.Label(playerReportFrame, text="Player Reports")
reportLabel.grid(row=0, column=0, sticky=tk.N)


# playerSearch
search_label = ttk.Label(search, text="Player Name")
search_label.pack(fill="x", expand=True)

search_entry = ttk.Entry(search, textvariable=playerSearch)
search_entry.pack(fill="x", expand=True)
search_entry.focus()

# watchlist
watchlist_label = ttk.Label(watchListFrame, text="Watch Players:")
watchlist_label.pack(fill="x", expand=True)

watchlist_entry = ttk.Entry(watchListFrame, textvariable=watchlistAdd)
watchlist_entry.pack(fill="x", expand=True)

# search button
search_button = ttk.Button(search, text="Search", command=login_clicked)
search_button.pack(fill="x", expand=True, pady=10)

# Watchlist Button Add
watchlist_button = ttk.Button(watchListFrame, text="Add", command=add_clicked)
watchlist_button.pack(fill="x", expand=True, pady=10)


watchlistRemove_button = ttk.Button(
    watchListFrame, text="Remove", command=remove_clicked
)
watchlistRemove_button.pack(fill="x", expand=True)

if watchList:
    time.sleep(20)
    for key in watchList:
        playerReports(key)


root.mainloop()