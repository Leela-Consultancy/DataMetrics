<?php

use Illuminate\Support\Facades\Route;

Route::get('/', function () {
    return view('index'); // Ensure 'index' matches the filename 'index.blade.php'
});