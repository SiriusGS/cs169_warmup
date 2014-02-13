class CreateUsers < ActiveRecord::Migration
  def up
  	drop_table :users
    create_table :users do |t|
      t.string :username
      t.string :password
      t.integer :count

      t.timestamps
    end
  end
end
