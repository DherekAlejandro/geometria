o
    ���b#  �                   @   sl   d dl mZ d dlmZmZmZmZmZ d dlm	Z	 d dl
Z
d dlmZ d dlmZmZmZmZ dd� ZdS )	�    )�text)�atan�cos�sin�sqrt�tan)�	text_fileN)�TRUE)�E�N�Y�Menuc            !   	   C   s�  t d� td�} | dks| dkrd}d}nttd��}td�}|dkr*d}t d	� nttd
��}ttd��}ttd��}ttd��}tt|d�t|d� d�}td| �}td| t|d� �}	t|	�}
|||  }tdt�|� �}t|�}tt�|| �d|
d|
    �}|td|
tt�|�d�  d� }t�||
| t�|�  | �}|td|
tt�|�d�  d� }t�||
| t�|�  | �}|td|
tt�|�d�  d� }t�||
| t�|�  | �}|td|
tt�|�d�  d� }t�||
| t�|�  | �}|t|� | }td�}|dk�s"|dk�r�tt�	|�d�}|dk �rYtt�
|��}td||  �}t|t�
|� d �}t dd|dt�
| �d| � n'tt�
|��}td||  �}t|t�
|� d �}t dd|dt�
|�d|� tt�	|�d�}|dk �r�tt�
|��}td||  �}t|t�
|� d �} t dd|dt�
| �d|  � n9tt�
|��}td||  �}t|t�
|� d �} t dd|dt�
|�d| � nt dt�	|�dt�	|�d|d|� t d|d|� d S )NzJESTE PROGRAMA CALCULA LAS COORDENADAS EN LONGITUD Y LATITUD DADAS UN X,Y,Zu3   ¿Trabajamos con el sistema de coordenadas WGS-84?
ZsiZSIi)  i�Sa zingrese f:
u   ¿el valor de a es:6´378.388?
u4    ¡Genial! es el valor con el que estamos trabajandoz	ingrese azIngrese la coordenada X:
zIngrese la coordenada Y:
zIngrese la coordenada Z:
�   g      �?�   u4   ¿Longitud y latitud en grados, minutos y segundos?
�   r   �<   zLONGITUD ES:zGrados: z	Minutos: z
Segundos: zLATITUD ES:zla longitud en decimal es:   z
la latitud en decimal es:   z
la altura es:   z
N es igual:  )�print�input�float�pow�mathr   r   r   �round�degrees�trunc)!�ws�f�a�A�x�y�z�p�Fr
   �e2ZlonZlongiZlongigraZYoZN1ZY1ZN2ZY2ZN3ZY3ZN4ZY4�hZASD�	Decimales�grados�minutos�segundosZ
Decimales1Zgrados1Zminutos1Z	segundos1� r)   �bc:\Users\Rayzen\OneDrive\Escritorio\clases\GEODESIA\ccosas\corte 1\PROBLEMA_DIRECTO_COORDENADAS.py�Problema_directo_coordenadas   sn   
"" " " " 
 
 "r+   )�cgitbr   �cmathr   r   r   r   r   �	distutilsr   r   �pickler	   �tkinterr
   r   r   r   r+   r)   r)   r)   r*   �<module>   s    