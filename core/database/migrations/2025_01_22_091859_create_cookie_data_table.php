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
        Schema::create('cookie_data', function (Blueprint $table) {
            $table->id();
            $table->string('name');
            $table->string('cookie_description')->nullable();
            $table->enum('cookie_type', ['firstparty', 'thirdparty'])->default('firstparty');
            $table->foreignId('vendor_id')->nullable()->constrained('vendors');
            $table->unsignedBigInteger('mapping_table_id')->nullable(); // Define column without foreign key
            $table->timestamps();
        });
    }

    /**
     * Reverse the migrations.
     */
    public function down(): void
    {
        Schema::dropIfExists('cookie_data');
    }
};
