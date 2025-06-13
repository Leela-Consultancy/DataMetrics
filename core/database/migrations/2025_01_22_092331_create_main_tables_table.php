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
        Schema::create('main_tables', function (Blueprint $table) {
            $table->id(); // This is already unsignedBigInteger by default
            $table->foreignId('website_id')->nullable()->constrained('websites')->onDelete('set null');
            $table->text('policy')->nullable();
            $table->string('cookie_category');
            $table->text('description');
            $table->timestamps();
        });
    }

    /**
     * Reverse the migrations.
     */
    public function down(): void
    {
        Schema::dropIfExists('main_tables');
    }
};
