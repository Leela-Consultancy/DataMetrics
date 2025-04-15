<?php

use Illuminate\Database\Migrations\Migration;
use Illuminate\Database\Schema\Blueprint;
use Illuminate\Support\Facades\Schema;

return new class extends Migration
{
    /**
     * Run the migrations.
     */
    public function up()
    {
        Schema::create('websites', function (Blueprint $table) {
            $table->id();
            $table->string('name');
            $table->enum('category', ['categoryone', 'categorytwo', 'categorythree'])->default('categoryone');
            $table->string('desc');
            $table->string('url');
            $table->text('privacy');
            $table->integer('strictly_necessary_cookies')->default(0);
            $table->integer('performance_cookies')->default(0);
            $table->integer('functionality_cookies')->default(0);
            $table->integer('targeting_cookies')->default(0);
            $table->integer('unknown_cookies')->default(0);
            $table->integer('persistent_cookies')->default(0);
            $table->integer('session_cookies')->default(0);
            $table->timestamps();
        });
    }

    public function down()
    {
        Schema::dropIfExists('websites');
    }
};
