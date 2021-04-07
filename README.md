# Tugas Kecil 3 STIMA 2021, Algoritma A star
> Algoritma A star dibuat dengan menggunakan bahasa python pada platform Jupyter notebook

## Table of contents
* [Dibuat](#dibuat)
* [General info](#general-info)
* [Setup](#setup)
* [Penggunaan](#penggunaan)
* [Status](#status)
* [Inspiration](#inspiration)

## Dibuat
Created by:
Nabil Nabighah (13519168)
Muhammad Furqon (13519184)

## General info
Algoritma A star dengan visualisasi map dengan ipyleaflet pada jupyter notebook

## Setup
* Install anaconda yang telah dilengkapi dengan jupyter notebook
* Install dependencies dalam anaconda dengan
'$ conda install -c conda-forge ipyleaflet'
* Buka file TucilStima.ipynb
* Pastikan cell pertama untuk instalasi conda package dalam jupyter kernel dapat berjalan
'import sys'
'!conda install --yes --prefix {sys.prefix} ipyleaflet'
* Run semua cell dan pada cell terakhir program utama dapat digunakan

## Penggunaan
Cara menggunakan
* Lakukan setup dan pastikan ipyleaflet dapat berfungsi
* Copy file yang ingin dibuka ke folder yang berisi .ipynb
* Run jupyter notebook
* Saat diminta memasukkan nama file, masukkan map.txt, matrix.txt, dan jarakreal.txt sesuai kebutuhan
* Saat visualisasi berhasil dapat menekan marker pada peta sebagai simpul awal, lalu menekan simpul lain sebagai simpul akhir
* Visualisasi rute terdekat akan muncul pada visualisasi peta

## Status
finished

## Inspiration
https://medium.com/@nicholas.w.swift/easy-a-star-pathfinding-7e6689c7f7b2
