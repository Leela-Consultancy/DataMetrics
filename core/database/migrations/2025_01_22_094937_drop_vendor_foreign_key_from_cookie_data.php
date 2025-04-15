<?php

use Illuminate\Database\Migrations\Migration;
use Illuminate\Database\Schema\Blueprint;
use Illuminate\Support\Facades\Schema;

return new class extends Migration
{
    /**
     * Run the migrations.
     */public function up()
    {
        Schema::table('cookie_data', function (Blueprint $table) {
            $table->dropForeign(['vendor_id']); // Drop the foreign key
            $table->dropColumn('vendor_id');   // Optional: Remove the column
        });
    }

    /**
     * Reverse the migrations.
     */
    public function down()
    {
        Schema::table('cookie_data', function (Blueprint $table) {
            $table->foreignId('vendor_id')->nullable()->constrained('vendors')->onDelete('set null');
        });
    }
};
