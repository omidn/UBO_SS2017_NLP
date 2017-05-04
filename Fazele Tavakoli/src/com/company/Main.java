package com.company;

import edu.stanford.nlp.ie.NERClassifierCombiner;
import edu.stanford.nlp.ling.CoreAnnotations;
import edu.stanford.nlp.tagger.maxent.MaxentTagger;
import java.io.*;

public class Main {
    public static void main(String[] args) {
        String filePath = "C:\\Users\\Apple\\IdeaProjects\\NLPLabFirstProject\\doc6.txt";
        Spliter spliter = new Spliter();
        Corpus.FileCleaner();
        try {
            String line = "";
            BufferedReader br = null;
            InputStream inputStream = new FileInputStream(filePath);
            br = new BufferedReader(new InputStreamReader(inputStream, "UTF-8"));
            while ((line = br.readLine()) != null) {
                line = line.replaceAll("[\uFEFF]", "");
                line = line.trim();
                String lines[] = spliter.lineSplitter(line);

                for (String singleLine : lines) {
                    if (!singleLine.isEmpty() && singleLine != "") {
                        String tagged = "";
                        //String a = "I like watching movies and you have moved very fast to my room";
                        MaxentTagger tagger = new MaxentTagger("C:\\Users\\Apple\\IdeaProjects\\NLPLabFirstProject\\POSTaggerModels\\models\\english-left3words-distsim.tagger");
                        tagged = tagger.tagString(singleLine);
                        String splittedSentence[] = spliter.sentenceSplitter(tagged);
                        for (String s : splittedSentence) {
                            //tagged = tagger.tagString(s);
                            for (int i = 0; i < s.length(); i++) {
                                if (s.charAt(i) == '_') {
                                    String wordSubString = s.substring(i + 1, s.length());
                                    wordSubString = wordSubString.trim();
                                    if (wordSubString.equals("JJ") || wordSubString.equals("JJR")
                                            || wordSubString.equals("JJS")) {
                                        wordSubString = "Adjective";
                                        System.out.println(s.substring(0, i) + ":" + wordSubString);
                                        Corpus.writeInFile(s.substring(0, i) + ":" + wordSubString);
                                        Corpus.writeInFile("\r\n");
                                    } else if (wordSubString.equals("NN") || wordSubString.equals("NNS") ||
                                            wordSubString.equals("NNP") || wordSubString.equals("NNPS")) {
                                        wordSubString = "Noun";
                                        System.out.println(s.substring(0, i) + ":" + wordSubString);
                                        Corpus.writeInFile(s.substring(0, i) + ":" + wordSubString);
                                        Corpus.writeInFile("\r\n");
                                    } else if (wordSubString.equals("RB") || wordSubString.equals("RBR") ||
                                            wordSubString.equals("RBS")) {
                                        wordSubString = "Adverb";
                                        System.out.println(s.substring(0, i) + ":" + wordSubString);
                                        Corpus.writeInFile(s.substring(0, i) + ":" + wordSubString);
                                        Corpus.writeInFile("\r\n");
                                    } else if (wordSubString.equals("VB") || wordSubString.equals("VBD") ||
                                            wordSubString.equals("VBG") || wordSubString.equals("VBN") || wordSubString.equals("VBP")
                                            || wordSubString.equals("VBZ")) {
                                        wordSubString = "Verb";
                                        System.out.println(s.substring(0, i) + ":" + wordSubString);
                                        Corpus.writeInFile(s.substring(0, i) + ":" + wordSubString);
                                        Corpus.writeInFile("\r\n");
                                    } else if (wordSubString.equals("RB") || wordSubString.equals("RBR") ||
                                            wordSubString.equals("RBS")) {
                                        wordSubString = "Adverb";
                                        System.out.println(s.substring(0, i) + ":" + wordSubString);
                                        Corpus.writeInFile(s.substring(0, i) + ":" + wordSubString);
                                        Corpus.writeInFile("\r\n");
                                    }
                                }
                            }
                        }


                        StanfordNER stanfordNER = new StanfordNER();
                        String singleLine1 = singleLine.trim();
                        /*String content="Sachin Ramesh Tendulkar (Listeni/ˌsətʃɪn tɛnˈduːlkər/; Marathi: "
                + " सचिन रमेश तेंडुलकर; born 24 April 1973) is an Indian former cricketer widely "
                + " acknowledged as the greatest batsman of the modern generation, popularly holds the title \"God of Cricket\" among his fans [2] He is also acknowledged as the greatest cricketer of all time.[6][7][8][9] He took up cricket at the age of eleven, made his Test debut against Pakistan at the age of sixteen, and went on to represent Mumbai domestically and India internationally for close to twenty-four years. He is the only player to have scored one hundred international centuries, the first batsman to score a Double Century in a One Day International, and the only player to complete more than 30,000 runs in international cricket.[10] In October 2013, he became the 16th player and first Indian to aggregate "
                + " 50,000 runs in all recognized cricket "
                + " First-class, List A and Twenty20 combined)";*/
                        System.out.println(stanfordNER.identifyNER(singleLine1, "C:\\Users\\Apple\\IdeaProjects\\NLPLabFirstProject\\NERModels\\classifiers\\english.conll.4class.distsim.crf.ser.gz").toString());
                        Corpus.writeInFile(stanfordNER.identifyNER(singleLine1, "C:\\Users\\Apple\\IdeaProjects\\NLPLabFirstProject\\NERModels\\classifiers\\english.conll.4class.distsim.crf.ser.gz").toString());
                    }
                }
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
