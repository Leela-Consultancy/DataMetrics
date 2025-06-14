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
        if (!Schema::hasTable('cookie_categories')) {
            Schema::create('cookie_categories', function (Blueprint $table) {
                $table->id();
                $table->string('name');
                $table->text('cookie_category_description');
                $table->foreignId('website_id')->nullable()->constrained()->onDelete('set null');
                $table->foreignId('main_table_id')->nullable()->constrained('main_tables')->onDelete('set null');
                $table->timestamps();
            });
        }
    }

    public function down()
    {
        Schema::dropIfExists('cookie_categories');
    }

};
