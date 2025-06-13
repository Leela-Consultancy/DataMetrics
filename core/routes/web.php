<?php

use Illuminate\Support\Facades\Route;


// routes/web.php
use App\Http\Controllers\WebsiteController;
use App\Http\Controllers\VendorController;
use App\Http\Controllers\CookieCategoryController;

Route::get('/', [WebsiteController::class, 'index'])->name('websites.index');
Route::post('/websites/paginate', [WebsiteController::class, 'paginate'])->name('websites.paginate');
Route::get('/websites/{website}', [WebsiteController::class, 'show'])->name('websites.show');
Route::get('/websites/search', [WebsiteController::class, 'search'])->name('websites.search');

Route::resource('vendors', VendorController::class);
Route::resource('cookie-categories', CookieCategoryController::class);
Route::resource('cookie-data', CookieDataController::class);

// routes/api.php
use App\Http\Controllers\Api\WebsiteController as ApiWebsiteController;

Route::prefix('v1')->group(function () {
    Route::get('/websites', [ApiWebsiteController::class, 'index']);
    Route::post('/websites', [ApiWebsiteController::class, 'store']);
    Route::get('/websites/{website}', [ApiWebsiteController::class, 'show']);
});
