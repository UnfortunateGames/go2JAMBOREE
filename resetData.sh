#!/bin/bash
rm PyFiles/settings/__settings__.txt PyFiles/backend/saveFile/__save__.txt
touch PyFiles/settings/__settings__.txt PyFiles/backend/saveFile/__save__.txt
cat defaulttxts/settings.txt > PyFiles/settings/__settings__.txt
cat defaulttxts/save.txt > PyFiles/backend/saveFile/__save__.txt