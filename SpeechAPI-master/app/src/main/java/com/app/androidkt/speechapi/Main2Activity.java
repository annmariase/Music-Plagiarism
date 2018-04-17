package com.app.androidkt.speechapi;

import android.content.ActivityNotFoundException;
import android.content.Intent;
import android.media.MediaPlayer;
import android.net.Uri;
import android.os.Environment;
import android.speech.RecognitionListener;
import android.speech.RecognizerIntent;
import android.speech.SpeechRecognizer;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.util.Log;
import android.view.Menu;
import android.view.MenuItem;
import android.view.View;
import android.widget.AdapterView;
import android.widget.ArrayAdapter;
import android.widget.BaseAdapter;
import android.widget.ImageButton;
import android.widget.ListView;
import android.widget.TextView;
import android.widget.Toast;

import java.io.File;
import java.util.ArrayList;
import java.util.Collection;
import java.util.HashMap;
import java.util.Locale;
import java.util.Set;

public class Main2Activity extends AppCompatActivity {
    HashMap<String,String> songList;
    ArrayList<String> songNameList;
    ArrayList<String> songPathList,searchNameList,searchPathList;
    private MediaPlayer mpintro;
    TextView textToSpeechResultField;
    SpeechRecognizer speechRecognizer;
    Intent speechRecognizerIntent;
    ListView listView;
    ArrayAdapter adapter;

    private final int REQ_CODE_SPEECH_INPUT = 100;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main2);

        songList = new HashMap<>();
        songNameList=null;
        songPathList=null;
        searchNameList=null;
        searchPathList=null;



        textToSpeechResultField=(TextView) findViewById(R.id.textToSpeechResultField);

        speechRecognizer=SpeechRecognizer.createSpeechRecognizer(this);
        speechRecognizerIntent = new Intent(RecognizerIntent.ACTION_RECOGNIZE_SPEECH);
        speechRecognizerIntent.putExtra(RecognizerIntent.EXTRA_LANGUAGE_MODEL,
                RecognizerIntent.LANGUAGE_MODEL_FREE_FORM);
        speechRecognizerIntent.putExtra(RecognizerIntent.EXTRA_LANGUAGE, Locale.getDefault());
        speechRecognizerIntent.putExtra(RecognizerIntent.EXTRA_PROMPT,"Musco Player");
        speechRecognizerIntent.putExtra(RecognizerIntent.EXTRA_LANGUAGE_MODEL,RecognizerIntent.LANGUAGE_MODEL_WEB_SEARCH);

        speechRecognizer.setRecognitionListener(new RecognitionListener() {
            @Override
            public void onReadyForSpeech(Bundle bundle) {

            }

            @Override
            public void onBeginningOfSpeech() {

            }

            @Override
            public void onRmsChanged(float v) {
                Log.i( "onRmsChanged: ","hello" );

            }

            @Override
            public void onBufferReceived(byte[] bytes) {

            }

            @Override
            public void onEndOfSpeech() {

            }

            @Override
            public void onError(int i) {

            }

            @Override
            public void onResults(Bundle bundle) {

            }

            @Override
            public void onPartialResults(Bundle bundle) {

            }

            @Override
            public void onEvent(int i, Bundle bundle) {

            }
        });

        try {

            songList = findSongs(Environment.getExternalStorageDirectory().getPath());

            Set<String> keySet = songList.keySet();
            songNameList=new ArrayList<String>(keySet);

            Collection<String> values = songList.values();
            songPathList = new ArrayList<String>(values);

            searchNameList=(ArrayList<String>)songNameList.clone();
            searchPathList=(ArrayList<String>)songPathList.clone();

        }catch (Exception e){

            Log.i("Error ", e.toString());
        }
        adapter = new ArrayAdapter<String>(this,
                R.layout.activity_listview,searchNameList);

        listView = (ListView) findViewById(R.id.mobile_list);
        listView.setAdapter(adapter);

        listView.setOnItemClickListener(new AdapterView.OnItemClickListener() {
            @Override
            public void onItemClick(AdapterView<?> adapterView, View view, int i, long l) {
                final String SelectedIteam=((TextView) view).getText().toString();
                int pos=songNameList.indexOf(SelectedIteam);
                final String FileLocation=songPathList.get(pos);
                Toast.makeText(Main2Activity.this,FileLocation,Toast.LENGTH_SHORT).show();
                playMusic(FileLocation);

            }
        });
    }
    HashMap<String,String> findSongs(String rootPath) {
        HashMap<String,String> fileList = new HashMap<>();
        try{
            File rootFolder = new File(rootPath);
            File[] files = rootFolder.listFiles(); //here you will get NPE if directory doesn't contains  any file,handle it like this.
            for (File file : files) {
                if (file.isDirectory()) {
                    if (findSongs(file.getAbsolutePath()) != null) {
                        fileList.putAll(findSongs(file.getAbsolutePath()));
                    } else {
                        break;
                    }
                } else if (file.getName().endsWith(".mp3")) {
                    fileList.put(file.getName().replace(".mp3",""),file.getAbsolutePath());
                }
            }
            return fileList;
        }catch(Exception e){
            Log.i("Member name: ", e.toString());
            return null;
        }
    }

    private void promptSpeechInput() {
        try {
            startActivityForResult(speechRecognizerIntent, REQ_CODE_SPEECH_INPUT);
        } catch (ActivityNotFoundException a) {
            Toast.makeText(getApplicationContext(),
                    "Not Supported",
                    Toast.LENGTH_SHORT).show();
        }
    }

    @Override
    protected void onActivityResult(int requestCode, int resultCode, Intent data) {
        super.onActivityResult(requestCode, resultCode, data);

        switch (requestCode) {
            case REQ_CODE_SPEECH_INPUT: {
                if (resultCode == RESULT_OK && null != data) {

                    ArrayList<String> result = data
                            .getStringArrayListExtra(RecognizerIntent.EXTRA_RESULTS);
                    String SpeechResult = result.get(0);

                    searchName(SpeechResult);

                    textToSpeechResultField.setText(SpeechResult);

                }
                break;
            }

        }
    }
    private void playMusic(String url) {
        /*+]
        mpintro = MediaPlayer.create(this, Uri.parse(url));
        mpintro.start();
        */
        Uri uri = Uri.parse(url);
        Intent intent = new Intent(Intent.ACTION_VIEW, uri);
        intent.setDataAndType(uri, "audio/*");
        startActivity(intent);
    }
    private void searchName(String string){
        searchNameList.clear();
        searchPathList.clear();
        searchNameList=(ArrayList<String>)songNameList.clone();
        searchPathList=(ArrayList<String>)songPathList.clone();
        Log.i("search",string);
        Log.i("size",""+searchPathList.size());
        int length=searchNameList.size();
        for (int i=0;i<length;i++) {
            if(!searchNameList.get(i).toLowerCase().contains(string.toLowerCase())){
                searchNameList.remove(i);
                searchPathList.remove(i);
                length=searchNameList.size();
                i--;
            }

        }
        Log.i("size",""+searchNameList.size());
        adapter = new ArrayAdapter<String>(this,
                R.layout.activity_listview,searchNameList);

        listView = (ListView) findViewById(R.id.mobile_list);
        listView.setAdapter(adapter);
        if(searchNameList.isEmpty()) {
            Log.i("search", "all empty");
            Toast.makeText(Main2Activity.this,"Song "+string+" not found",Toast.LENGTH_SHORT).show();
        }
    }
++
    @Override
    public boolean onCreateOptionsMenu(Menu menu) {
        getMenuInflater().inflate(R.menu.mainmenu,menu);
        return super.onCreateOptionsMenu(menu);
    }
    @Override
    public boolean onOptionsItemSelected(MenuItem item) {
        if(item.getItemId()==R.id.reload) {
            searchNameList.clear();
            searchPathList.clear();
            searchNameList=(ArrayList<String>)songNameList.clone();
            searchPathList=(ArrayList<String>)songPathList.clone();
            adapter = new ArrayAdapter<String>(this,
                    R.layout.activity_listview,searchNameList);

            listView = (ListView) findViewById(R.id.mobile_list);
            listView.setAdapter(adapter);

        }
        //speechToTextButton
        else  if(item.getItemId()==R.id.search) {
            promptSpeechInput();
        }
        return super.onOptionsItemSelected(item);
    }


}
