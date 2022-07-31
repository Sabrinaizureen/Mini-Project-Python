from msilib.schema import Font
from tkinter import*
from tkinter import Tk, StringVar, ttk
from tkinter import messagebox
from turtle import right
from tkcalendar import Calendar
import sqlite3
from PIL import Image, ImageTk

window = Tk()
window['bg']='black'
window.geometry("1350x700")
window.title("Bus Online Booking")