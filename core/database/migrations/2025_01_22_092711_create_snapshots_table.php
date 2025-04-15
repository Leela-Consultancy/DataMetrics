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
        Schema::create('snapshots', function (Blueprint $table) {
            $table->id();
            $table->string('name');
            $table->string('cookie_category');
            $table->text('cookie_category_description');
            $table->foreignId('website_id')->nullable()->constrained();
            $table->foreignId('main_table_id')->nullable()->constrained('main_tables');
            $table->foreignId('cookie_data_id')->nullable()->constrained('cookie_data');
            $table->string('cookie_description')->nullable();
            $table->enum('cookie_type', ['firstparty', 'thirdparty'])->default('firstparty');
            $table->foreignId('vendor_id')->nullable()->constrained('vendors');
            $table->foreignId('mapping_table_id')->nullable()->constrained('mapping_tables');
            $table->text('privacy_id');
            $table->text('privacy_policy_data');
            $table->string('vendor_site_brief');
            $table->string('vendor_url');
            $table->timestamps();
        });
    }
    /**
     * Reverse the migrations.
     */
    public function down(): void
    {
        Schema::dropIfExists('snapshots_tables');
    }
};
