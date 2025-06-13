<?php

use Illuminate\Database\Migrations\Migration;
use Illuminate\Database\Schema\Blueprint;
use Illuminate\Support\Facades\Schema;

class CreateCookieCategoriesTable extends Migration
{
    /**
     * Run the migrations.
     *
     * @return void
     */
    public function up()
    {
        Schema::create('cookie_categories', function (Blueprint $table) {
            $table->id();
            // ...existing code...
            $table->unsignedBigInteger('main_table_id')->nullable();
            $table->foreign('main_table_id')
                  ->references('id')
                  ->on('main_tables')
                  ->onDelete('set null');
            // ...existing code...
            $table->timestamps();
        });
    }

    /**
     * Reverse the migrations.
     *
     * @return void
     */
    public function down()
    {
        Schema::dropIfExists('cookie_categories');
    }
}