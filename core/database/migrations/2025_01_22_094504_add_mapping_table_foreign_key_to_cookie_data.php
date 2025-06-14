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
        Schema::table('cookie_data', function (Blueprint $table) {
            $table->foreign('mapping_table_id')->references('id')->on('mapping_tables')->onDelete('set null');
        });
    }

    /**
     * Reverse the migrations.
     */
    public function down()
    {
        Schema::table('cookie_data', function (Blueprint $table) {
            $table->dropForeign(['mapping_table_id']);
        });
    }

};
