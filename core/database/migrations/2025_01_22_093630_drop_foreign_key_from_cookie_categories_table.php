<?php

use Illuminate\Database\Migrations\Migration;
use Illuminate\Database\Schema\Blueprint;
use Illuminate\Support\Facades\Schema;


class DropForeignKeyFromCookieCategoriesTable extends Migration
{
    public function up()
    {
        Schema::table('cookie_categories', function (Blueprint $table) {
            $table->dropForeign(['website_id']); // Drop the foreign key
        });
    }

    public function down()
    {
        Schema::table('cookie_categories', function (Blueprint $table) {
            $table->foreign('website_id')->references('id')->on('websites')->onDelete('set null');
        });
    }
}
